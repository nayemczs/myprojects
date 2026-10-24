"""
Authors: TANZIM AHMED and NAYEMUL ISLAM MAJUMDER
Author Emails: tanzim.din@northsouth.edu and nayemul.majumder@northsouth.edu
Created on: 17th July 2020
For: readmearticles.com

A Flask application to convert HTML articles into speech.
"""


import os
from . import keys


# BASE DIR
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Default Mail Sender
MAIL_DEFAULT_SENDER = "david@thepowerlist.app"


# Minimum Article Length including Title
MIN_ARTICLE_LENGTH = 250


# HEX Token byte length for audio filenames (1 byte = 2 HEX characters)
TOKEN_LENGTH = 16


# Run without AWS and DigitalOcean calls (for development purpose)
TEST_RUN_WITHOUT_AWS = False


# Digital Ocean - Spaces Configurations
SPACES_KEY = keys.SPACES_KEY
SPACES_SECRET = keys.SPACES_SECRET
SPACES_REGION = 'sfo2'
SPACES_ENDPOINT_URL = f'https://{SPACES_REGION}.digitaloceanspaces.com'
SPACES_STORAGE_NAME = 'readme'
SPACES_URL_EXPIRATION_TIME = 300    # For Spaces private URLs.
SPACES_ACL = 'public-read'


# AWS Configurations
AWS_ACCESS_KEY_ID = keys.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = keys.AWS_SECRET_ACCESS_KEY
AWS_REGION = 'us-east-1'
AWS_VOICE_ID = 'Joanna'
AWS_OUTPUT_FORMAT = 'mp3'


# APP Media URL
MEDIA_URL = f'https://{SPACES_STORAGE_NAME}.{SPACES_REGION}.digitaloceanspaces.com'
# https://readme.sfo2.digitaloceanspaces.com


# For storing temporary audio files
TEMP_DIR = 'temp'


# APP default configs
APP_CONFIGS = {
    # APP secret key
    'SECRET_KEY': keys.SECRET_KEY,

    # SQL_Alchemy configurations
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + os.path.join(BASE_DIR, 'database', 'db.sqlite3'),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,

    # APP Security configurations
    'SECURITY_PASSWORD_SALT': keys.SECURITY_PASSWORD_SALT,
    'SECURITY_RECOVERABLE': True,
    'SECURITY_CHANGEABLE': True,
    'SECURITY_REGISTERABLE': True,
    'SECURITY_CONFIRMABLE': False,  # Temporarily disabled
    'SECURITY_EMAIL_SENDER': MAIL_DEFAULT_SENDER,

    # Mail Configurations
    'MAIL_SERVER': 'smtp.ionos.com',
    'MAIL_PORT': 465,
    'MAIL_USE_SSL': True,
    'MAIL_USERNAME': '*@thepowerlist.app',
    'MAIL_PASSWORD': keys.MAIL_PASSWORD,
    'MAIL_DEFAULT_SENDER': MAIL_DEFAULT_SENDER
}
