import pytest
from webtest import TestApp

from website import create_app


@pytest.fixture(scope='session')
def app_config():
    """The config for the test application"""
    settings = {
        'TESTING': True,
        'SECRET_KEY': 'a key for testing',
        'DEBUG': False,
    }

    return settings


@pytest.yield_fixture(scope='session')
def app(app_config):
    """The test application"""
    _app = create_app()
    _app.config.update(app_config)

    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def test_client(app):
    """
    Configure a WebTest client for nice convenience methods."""
    return TestApp(app)
