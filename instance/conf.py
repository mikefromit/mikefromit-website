import os
import uuid

import redis

from website.utils import make_database_url


# SETTINGS

# MAIN FLASK APPLICATION
DEBUG = os.environ.get('FLASK_DEBUG', False)
SECRET_KEY = os.environ.get('SESSION_SECRET', str(uuid.uuid4()))

# REDIS
SESSION_TYPE = 'redis'
SESSION_REDIS = redis.Redis('redis')

# Flask-SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = make_database_url()

# Flask-Security
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_SALT', 'development_secret')
SECURITY_CONFIRMABLE = False
SECURITY_REGISTERABLE = False
SECURITY_RECOVERABLE = True
SECURITY_TRACKABLE = True
SECURITY_CHANGEABLE = True
SECURITY_EMAIL_SENDER = os.environ.get('SECURITY_EMAIL_SENDER', '')

