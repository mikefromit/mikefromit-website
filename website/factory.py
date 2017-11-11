from flask import Flask
from flask_security import SQLAlchemyUserDatastore

from .core import db, security
from .helpers import register_blueprints
from .models import User, Role
from .redis_session import RedisSessionInterface


def create_app(package_name, package_path, settings=None):
    """
    This function creates the application using the application factory pattern.
    Extensions and blueprints are then initialized onto the the application
    object.

    http://flask.pocoo.org/docs/0.11/patterns/appfactories/

    :param package_name: the name of the package
    :param package_path: the path of the package
    :param settings: override default settings via a python object
    :return: app: the main flask application object
    """

    app = Flask(package_name,
                instance_relative_config=True,
                template_folder='templates')

    app.config.from_pyfile('conf.py', silent=True)

    if settings:
        app.config.update(settings)

    # Init Extensions
    db.init_app(app)
    app.security = security.init_app(app,
                                     SQLAlchemyUserDatastore(db, User, Role),
                                     register_blueprint=True)

    # Use redis sessions
    app.session_interface = RedisSessionInterface()

    # Helper for auto-registering blueprints
    register_blueprints(app, package_name, package_path)

    return app
