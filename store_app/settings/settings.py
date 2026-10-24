from pathlib import Path
from . import keys
import os
import stripe


# Base Directory of the project.
BASE_DIR = Path(__file__).parent.parent


# Site URL
SITE_URL = 'http://127.0.0.1:5000'


# Stripe API Key
STRIPE_PUBLIC_KEY = keys.STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY = keys.STRIPE_SECRET_KEY
STRIPE_WEBHOOK_SECRET = keys.STRIPE_WEBHOOK_SECRET
stripe.api_key = STRIPE_SECRET_KEY


# APP Configurations
APP_CONFIGS = {
    'SECRET_KEY': keys.SECRET_KEY,

    # SQL_Alchemy configurations
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,

    # Flask Security
    'SECURITY_PASSWORD_SALT': keys.SECURITY_PASSWORD_SALT,
    'SECURITY_REGISTERABLE': True,
    'SECURITY_REGISTER_URL': '/register/',
    'SECURITY_SEND_REGISTER_EMAIL': False,
    'SECURITY_REGISTER_USER_TEMPLATE': 'pages/sign_up.html',
    'SECURITY_LOGIN_URL': '/login/',
    'SECURITY_LOGIN_USER_TEMPLATE': 'pages/login.html'
}
