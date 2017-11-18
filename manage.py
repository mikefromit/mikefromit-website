import click
from datetime import datetime

from flask import current_app
from flask_security import utils

from website import create_app
from website.core import db

app = create_app()


@app.cli.command()
@click.confirmation_option(
    prompt='This will erase everything in the database. Do you want to continue?')
def reset_db():
    """Resets the database to the original state using alembic downgrade and upgrade commands"""
    from alembic.command import downgrade, upgrade
    from alembic.config import Config as AlembicConfig
    config = AlembicConfig('alembic.ini')
    downgrade(config, 'base')
    upgrade(config, 'head')
    print('Database has been reset')


@app.cli.command()
@click.option('--email', prompt=True)
@click.password_option('--password')
def create_admin_user(email, password):
    """Create an admin user to be used to login to the database initially."""
    user_datastore = current_app.extensions['security'].datastore
    user_datastore.find_or_create_role(name='admin',
                                       description='Administrator')
    encrypted_password = utils.hash_password(password)

    if not user_datastore.get_user(email):
        user_datastore.create_user(email=email,
                                   active=True,
                                   registered_at=datetime.now(),
                                   confirmed_at=datetime.now(),
                                   password=encrypted_password)
    db.session.commit()
    user_datastore.add_role_to_user(email, 'admin')
    db.session.commit()


@app.cli.command()
def send_test_email():
    """Send a test email."""
    from flask_mail import Message
    from website.core import mail

    to = ['no-reply@mikefromit.com']
    subject = 'Test Email'
    template = '<h1>You Ok?</h1>'

    msg = Message(
        subject,
        recipients=to,
        html=template,
        sender=current_app.config['SECURITY_EMAIL_SENDER']
    )
    mail.send(msg)


if __name__ == '__main__':
    app.cli()
