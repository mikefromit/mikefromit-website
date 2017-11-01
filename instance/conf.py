import os

# MAIN FLASK APPLICATION
DEBUG = os.environ.get('FLASK_DEBUG', False)

# REDIS
REDIS_URL = os.environ.get('REDIS_URL', None)
