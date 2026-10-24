from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore
from flask_security.utils import hash_password
import stripe
from settings.settings import SITE_URL

db = SQLAlchemy()


class EntityInterface:
    id = None

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


users_purchases = db.Table(
    'users_purchases',
    db.Column('profile_id', db.Integer(), db.ForeignKey('user_profile.id')),
    db.Column('product_id', db.Integer(), db.ForeignKey('product.id'))
)


class UserProfile(db.Model, EntityInterface):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    customer_id = db.Column(db.String(255), nullable=True)
    products = db.relationship(
        'Product',
        secondary=users_purchases,
        backref=db.backref('user_profiles', lazy='dynamic')
    )


class User(db.Model, UserMixin, EntityInterface):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    confirmed_at = db.Column(db.DateTime())
    is_active = db.Column(db.Boolean())
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    user_profile = db.relationship('UserProfile', backref=db.backref('user', uselist=False), uselist=False)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    user_profile_class = UserProfile

    def __init__(self, email, password, first_name, last_name, active=False, is_admin=False, roles=None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = active
        self.is_admin = is_admin
        self.roles = roles

    def set_password(self, password):
        self.password = hash_password(password)

    @classmethod
    def create_dummy_user(cls):
        if not cls.query.all():
            user = cls(
                email='user_1@test.com',
                password='12345678',
                first_name='Demo',
                last_name='User 1',
                active=True,
                roles=[]
            )
            user.set_password(user.password)
            user.save()
            return user

    def get_user_profile(self):
        if not self.user_profile:
            self.user_profile = self.user_profile_class()
            self.save()
        return self.user_profile

    def __str__(self):
        return f'({self.id}) {self.first_name} {self.last_name}'


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return f'({self.id}) {self.name}'


class Product(db.Model, EntityInterface):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    price = db.Column(db.Float())
    quantity = db.Column(db.Float())
    site_url = SITE_URL

    def __init__(self, name, image_url, price, quantity):
        self.name = name
        self.image_url = image_url
        self.price = price
        self.quantity = quantity

    @classmethod
    def process_checkout(cls, session_id, product_id, profile):
        session = stripe.checkout.Session.retrieve(session_id)
        product = cls.query.get(product_id)

        product.quantity -= 1
        product.save()

        profile.customer_id = session.customer
        profile.products.append(product)
        profile.save()

    @classmethod
    def create_checkout(cls, product_id, user_email):
        product = cls.query.get(product_id)

        line_items = [
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(product.price * 100),
                    'product_data': {
                        'name': product.name,
                        'images': [product.image_url],
                    },
                },
                'quantity': 1,
            },
        ]

        checkout_session = stripe.checkout.Session.create(
            success_url=cls.site_url + '/checkout/success/{CHECKOUT_SESSION_ID}/' + product_id + '/',
            cancel_url=cls.site_url + '/checkout/canceled/',
            customer_email=user_email,
            payment_method_types=['card'],
            mode='payment',
            line_items=line_items
        )
        return checkout_session['id']

    @classmethod
    def create_dummy_product(cls, quantity=10):
        if not cls.query.all():
            product = cls(
                name='Dummy Product',
                image_url='https://i.imgur.com/EHyR2nP.png',
                price=25.00,
                quantity=quantity
            )
            product.save()
            return product


user_data_store = SQLAlchemyUserDatastore(db, User, Role)
