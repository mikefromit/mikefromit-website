from flask_mail import Mail
from flask_session import Session
from flask_security import Security
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

mail = Mail()

security = Security()

sess = Session()
