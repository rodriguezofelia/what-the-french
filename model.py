"""Models for french conjugation app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    created_at = db.Column((db.datetime, default=datetime.datetime.utcnow), nullable=False)
    modified_at = db.Column((db.datetime, default=datetime.datetime.utcnow), nullable=False)
    password = db.Column(db.Text, nullable=False)


class Grade(db.Model):
    """Grade(s) for a given user."""

    __tablename__ = "grades"

    grade_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    created_at = db.Column((db.datetime, default=datetime.datetime.utcnow), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.quiz_id'), nullable=False)
    
    user = db.relationship('User', backref='grades')
    quiz = db.relatinoship('Quiz', backref='grades')



