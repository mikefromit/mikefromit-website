import os

# MAIN FLASK APPLICATION
DEBUG = os.environ.get('FLASK_DEBUG', False)

# REDIS
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
