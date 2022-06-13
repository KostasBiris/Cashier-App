from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Money(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    oneHundred = db.Column(db.Integer)
    fifty = db.Column(db.Integer)
    twenty = db.Column(db.Integer)
    ten = db.Column(db.Integer)
    total = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    store_name = db.Column(db.String(150))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    staffcode = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))