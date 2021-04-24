"""Models for french conjugation app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True,unique=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    created_at = db.Column((db.datetime, default=datetime.datetime.utcnow), nullable=False)
    modified_at = db.Column((db.datetime, default=datetime.datetime.utcnow), nullable=False)
    password = db.Column(db.Text, nullable=False)



