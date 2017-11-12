import os


def make_database_url():
    return 'postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(
        os.environ.get('DB_USER', 'postgres'),
        os.environ.get('DB_PASSWORD', ''),
        os.environ.get('DB_HOST', '127.0.0.1'),
        os.environ.get('DB_PORT', '5432'),
        os.environ.get('DB_NAME', 'tests'),
    )
