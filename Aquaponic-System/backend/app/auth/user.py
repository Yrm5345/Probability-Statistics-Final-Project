from flask_login import UserMixin
from .. import db # do not import anywhere else 
class User(db.Model, UserMixin):
    username = db.Column(db.String(120), unique=True, nullable=False , primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(120), unique=True, nullable=False)


