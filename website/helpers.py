import importlib
import pkgutil

import os
from flask import Blueprint


def register_blueprints(app, package_name, package_path):  # pragma: no cover
    """
    Register all Blueprint instances on the specified Flask application found
    in all modules for any found package

    :param app: the Flask application
    :param package_name: the package name
    :param package_path: the package path
    :return:
    """
    rv = []
    base_dir = package_path[0]
    for _, pkgname, ispkg in pkgutil.walk_packages([base_dir]):
        for _, modname, ismod in pkgutil.iter_modules(
                [os.path.join(base_dir, pkgname)]):
            m = importlib.import_module(
                '{0}.{1}.{2}'.format(package_name, pkgname, modname))
            for item in dir(m):
                item = getattr(m, item)
                if isinstance(item, Blueprint):
                    app.register_blueprint(item)
                rv.append(item)

    return rv
