"""
Authors: TANZIM AHMED and NAYEMUL ISLAM MAJUMDER
Author Emails: tanzim.din@northsouth.edu and nayemul.majumder@northsouth.edu
Created on: 25th July 2020
For: hunchgroup.com

A Flask web application for Real Estate company.
"""

import os

# Settings file

# Project base directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Mail Default Service
MAIL_DEFAULT_SERVICE = 'mail_gun_api'

# Default Mail Sender
MAIL_DEFAULT_SENDER = 'Hunch Group <team@hunchgroup.com>'

# Admin Email
ADMIN_EMAIL = 'alldayhouses@gmail.com'

# MailGun Settings
MAIL_GUN_URL = os.environ.get('MAIL_GUN_URL', '')
MAIL_GUN_API_KEY = os.environ.get('MAIL_GUN_API_KEY', '')

APP_CONFIGS = {
    'SECRET_KEY': os.environ.get('SECRET_KEY', 'dev-secret-key-real-estate-change-in-production'),

    # SQL_Alchemy configurations
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + os.path.join(BASE_DIR, 'database', 'db.sqlite3'),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,

    # Flask Security
    'SECURITY_PASSWORD_SALT': os.environ.get('SECURITY_PASSWORD_SALT', 'dev-salt-real-estate-change-in-production'),
    'SECURITY_LOGIN_URL': '/admin/login/',
    'SECURITY_LOGOUT_URL': '/admin/logout/',
    'SECURITY_POST_LOGIN_VIEW': '/admin/',
    'SECURITY_POST_LOGOUT_VIEW': '/admin/login/',

    # Mail Configurations
    'MAIL_SERVER': '',
    'MAIL_PORT': 587,
    'MAIL_USE_TLS': True,
    'MAIL_USE_SSL': False,
    'MAIL_USERNAME': MAIL_DEFAULT_SENDER,
    'MAIL_PASSWORD': os.environ.get('MAIL_PASSWORD', ''),
    'MAIL_DEFAULT_SENDER': MAIL_DEFAULT_SENDER
}
