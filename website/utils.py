import os


def make_database_url():
    # Check for DATABASE_URL that is provided by heroku
    if 'DATABASE_URL' in os.environ and os.environ['DATABASE_URL']:
        return os.environ.get('DATABASE_URL')
    else:
        return 'postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(
            os.environ.get('DB_USER', 'postgres'),
            os.environ.get('DB_PASSWORD', ''),
            os.environ.get('DB_HOST', '127.0.0.1'),
            os.environ.get('DB_PORT', '5432'),
            os.environ.get('DB_NAME', 'tests'),
        )
