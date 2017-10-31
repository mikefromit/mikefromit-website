from . import factory


def create_app(settings=None):
    return factory.create_app(__name__, __path__, settings)

