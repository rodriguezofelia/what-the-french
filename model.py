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


class Quiz(db.Model):
    """Quiz user can take."""

    __tablename__ = "quizzes"

    quiz_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    quiz_name = db.Column(db.Text, nullable=False)
    verb_id = db.Column(db.Integer, db.ForeignKey('DOESNT EXIST YET'), nullable=False)
    tense_id = db.Column(db.Integer, db.ForeignKey('DOESNT EXIST YET'), nullable=False)

    verb = db.relationship('DOESNT EXIST YET', backref='quizzes')
    temse = db.relatinoship('DOESNT EXIST YET', backref='quizzes')


class Quiz_Sentence(db.Model):
    """Sentences that make up each Quiz."""

    __tablename__ = "quiz_sentences"

    quiz_sentence_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.quiz_id'), nullable=False)
    sentence_id = db.Column(db.Integer, db.ForeignKye('DOESNT EXIST YET'), nullable=False)

    quiz = db.relationship('Quiz', backref='quiz_sentences')
    sentence = db.relationship('DOESNT EXIST YET', backref='quiz_sentences')

