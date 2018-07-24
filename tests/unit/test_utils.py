import os

from website.utils import make_database_url


def test_make_database_url():
    # Test default
    url = make_database_url()
    assert url == 'postgresql+psycopg2://postgres:@127.0.0.1:5432/tests'
    # Set Env Var to see if it changes
    os.environ['DATABASE_URL'] = 'postgresql+psycopg2://postgres:@127.0.0.1:5433/testdb'
    url = make_database_url()
    assert url == 'postgresql+psycopg2://postgres:@127.0.0.1:5433/testdb'
