from qa327 import app
from flask_sqlalchemy import SQLAlchemy

"""
This file defines all models used by the server
These models provide us a object-oriented access
to the underlying database, so we don't need to 
write SQL queries such as 'select', 'update' etc.
"""


db = SQLAlchemy()
db.init_app(app)


class User(db.Model):
    """
    A user model which defines the sql table
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
  #  balance = db.Column(db.Integer) - you can't add paramters!


class Tickets(db.Model):
    ticket_id = db.Column(db.Integer, primary_key=True)
    ticket_name = db.Column(db.String(1000), unique=True)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    expiration_date = db.Column(db.String(100))


# it creates all the SQL tables if they do not exist
with app.app_context():
    db.create_all()
    db.session.commit()
