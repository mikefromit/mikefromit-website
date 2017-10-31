import os

from website import create_app

app = create_app()


if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT', 5000))
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    app.run(host=host, port=port)
