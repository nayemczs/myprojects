from app import app, database
from json import loads as parse_json
from unittest import main, TestCase
import os
from core.models import Product, User
from settings.settings import BASE_DIR, STRIPE_PUBLIC_KEY


class TestApp(TestCase):

    def setUp(self) -> None:
        # Set Up test database
        # Disable CSRF_TOKEN while testing to send POST request to the server easily!
        self.database_path = os.path.join(BASE_DIR, 'db_test.sqlite3')
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + self.database_path
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['TESTING'] = True
        self.client = app.test_client(self)
        with app.app_context():
            database.create_all(app=app)
            Product.create_dummy_product(quantity=20)
            User.create_dummy_user()

    def tearDown(self) -> None:
        # Remove test database
        try:
            os.remove(self.database_path)
        except FileNotFoundError:
            pass

    def test_test_database_entries_created(self):
        # Check test database is being used
        with app.app_context():
            self.assertTrue(Product.query.first().quantity == 20)
            self.assertTrue(User.query.first().email == 'user_1@test.com')

    def test_index(self):
        # Test loads index page
        response = self.client.get('/')
        self.assertTrue(b'Dummy Product' in response.data)

    def test_register(self):
        # Test loads login page
        response = self.client.get('/register/')
        self.assertTrue(b'First Name' in response.data)

        # Test cannot create user with same emails
        response = self.client.post('/register/', data={
            'first_name': 'Demo',
            'last_name': 'User 1',
            'email': 'user_1@test.com',
            'password': '12345678',
            'password_confirm': '12345678'
        }, follow_redirects=True)
        self.assertTrue(b'user_1@test.com is already associated with an account.' in response.data)

        # Test checks if password field matches with confirmation
        response = self.client.post('/register/', data={
            'first_name': 'Demo',
            'last_name': 'User 2',
            'email': 'user_2@test.com',
            'password': '12345678',
            'password_confirm': '1234567'
        }, follow_redirects=True)
        self.assertTrue(b'Passwords do not match' in response.data)

        # Test user gets registered
        response = self.client.post('/register/', data={
            'first_name': 'Demo',
            'last_name': 'User 2',
            'email': 'user_2@test.com',
            'password': '12345678',
            'password_confirm': '12345678'
        }, follow_redirects=True)
        self.assertTrue(b'Buy' in response.data)
        self.assertTrue(b'Logout' in response.data)

    def test_login_and_logout(self):
        # Test login page loads
        response = self.client.get('/login/')
        self.assertFalse(b'First Name' in response.data)
        self.assertTrue(b'email' in response.data)

        # Test user can login
        response = self.login_user()
        self.assertTrue(b'Buy' in response.data)
        self.assertTrue(b'Logout' in response.data)

        # Test user can logout
        response = self.client.get('/logout/', follow_redirects=True)
        self.assertFalse(b'Buy' in response.data)
        self.assertFalse(b'Logout' in response.data)
        self.assertTrue(b'Login' in response.data)
        self.assertTrue(b'Register' in response.data)

    def test_login_fails_with_invalid_credentials(self):
        # Test login get prohibited with invalid credentials
        response = self.client.post('/login/', data={
            'email': 'user_2@test.com',
            'password': '12345678'
        }, follow_redirects=True)
        self.assertTrue(b'email' in response.data)
        self.assertTrue(b'Specified user does not exist' in response.data)

        response = self.client.post('/login/', data={
            'email': 'user_1@test.com',
            'password': '1234567'
        }, follow_redirects=True)
        self.assertTrue(b'email' in response.data)
        self.assertFalse(b'Specified user does not exist' in response.data)
        self.assertTrue(b'Invalid password' in response.data)

    def test_checkout_sessions_get_created_or_cancelled(self):
        # Test Stripe PUBLIC KEY is loaded when user is logged in
        self.login_user()
        response = self.client.get('/')
        self.assertTrue(bytes(STRIPE_PUBLIC_KEY, encoding='ascii') in response.data)

        # Test Stripe Checkout session gets created
        response = self.client.post('/checkout/create/', data={'product_id': 1})
        data = parse_json(response.data)
        self.assertTrue(data.get('sessionId'))

    def test_product_gets_added_to_user_purchases_on_checkout_success(self):
        # Test cannot check out without login
        # Use the SESSION ID of a successful checkout session from stripe dashboard
        stripe_session_id = 'cs_test_a1vei4F63ZBwKpJ45qG8N9hRzquocbi40nA0RcBRW6lW9V5Lxo146cD1Go'

        response = self.client.get(
            f'/checkout/success/{stripe_session_id}/1/',
            follow_redirects=True
        )
        self.assertTrue(b'email' in response.data)
        self.assertTrue(b'password' in response.data)

        # Test database is updated with successful checkout
        self.login_user()
        response = self.client.get(
            f'/checkout/success/{stripe_session_id}/1/',
            follow_redirects=True
        )
        with app.app_context():
            product = Product.query.get(1)
            user_profile = User.query.first().get_user_profile()
            self.assertTrue(product in user_profile.products)
            self.assertEqual(product.quantity, 19)
            self.assertIsNotNone(user_profile.customer_id)

    def login_user(self):
        return self.client.post('/login/', data={
            'email': 'user_1@test.com',
            'password': '12345678'
        }, follow_redirects=True)


if __name__ == '__main__':
    main()
