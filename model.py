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
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    modified_at = db.Column(db.DateTime, default=datetime.utcnow())
    password = db.Column(db.Text, nullable=False)


class Grade(db.Model):
    """Grade(s) for a given user."""

    __tablename__ = "grades"

    grade_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    grade = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.quiz_id'), nullable=False)
    
    user = db.relationship('User', backref='grades')
    quiz = db.relationship('Quiz', backref='grades')


class Quiz(db.Model):
    """Quiz user can take."""

    __tablename__ = "quizzes"

    quiz_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    quiz_name = db.Column(db.Text, nullable=False)
    verb_id = db.Column(db.Integer, db.ForeignKey('verbs.verb_id'), nullable=False)
    tense_id = db.Column(db.Integer, db.ForeignKey('tenses.tense_id'), nullable=False)

    verb = db.relationship('Verb', backref='quizzes')
    temse = db.relationship('Tense', backref='quizzes')


class Quiz_Sentence(db.Model):
    """Sentences that make up each Quiz."""

    __tablename__ = "quiz_sentences"

    quiz_sentence_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.quiz_id'), nullable=False)
    sentence_id = db.Column(db.Integer, db.ForeignKey('sentences.sentence_id'), nullable=False)

    quiz = db.relationship('Quiz', backref='quiz_sentences')
    sentence = db.relationship('Sentence', backref='quiz_sentences')


class Verb(db.Model):
    """Verbs to select from."""

    __tablename__ = "verbs"

    verb_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    verb = db.Column(db.Text, nullable=False)


class Tense(db.Model):
    """Tenses to select from."""

    __tablename__ = "tenses"

    tense_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    tense = db.Column(db.Text, nullable=False)


class Conjugated_Verb(db.Model): 
    """Correct conjugation of verbs."""

    __tablename__ = "conjugated_verbs"

    conjugated_verb_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    conjugated_verb = db.Column(db.Text, nullable=False)
    verb_id = db.Column(db.Integer, db.ForeignKey('verbs.verb_id'), nullable=False)
    tense_id = db.Column(db.Integer, db.ForeignKey('tenses.tense_id'), nullable=False)
    subject_pronoun = db.Column(db.Text, nullable=False)

    verb = db.relationship('Verb', backref='conjugated_verbs')
    tense = db.relationship('Tense', backref='conjugated_verbs')


class Sentence(db.Model): 
    """Sentences that the User gets answer in Quiz_Sentences."""

    __tablename__ = "sentences"

    sentence_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    blank_word_sentence = db.Column(db.Text, nullable=False)
    conjugated_verb_id = db.Column(db.Integer, db.ForeignKey('conjugated_verbs.conjugated_verb_id'), nullable=False)

    conjugated_verb_id = db.relationship('Sentence', backref='sentences')