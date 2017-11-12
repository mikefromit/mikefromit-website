from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security


db = SQLAlchemy()

mail = Mail()

security = Security()

