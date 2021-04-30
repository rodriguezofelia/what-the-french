"""Models for french conjugation app."""

from flask import Flask
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

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email} first_name={self.first_name} last_name={self.last_name}>'


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

    def __repr__(self):
        return f'<User grade_id={self.grade_id} grade={self.grade} user_id={self.user_id} quiz_id={self.quiz_id}>'

class Quiz(db.Model):
    """Quiz user can take."""

    __tablename__ = "quizzes"

    quiz_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    quiz_name = db.Column(db.Text, nullable=False)
    verb_id = db.Column(db.Integer, db.ForeignKey('verbs.verb_id'), nullable=False)
    tense_id = db.Column(db.Integer, db.ForeignKey('tenses.tense_id'), nullable=False)

    verb = db.relationship('Verb', backref='quizzes')
    temse = db.relationship('Tense', backref='quizzes')

    def __repr__(self):
        return f'<User quiz_id={self.quiz_id} quiz_name={self.quiz_name} verb_id={self.verb_id} tense_id={self.tense_id}>'


class Quiz_Sentence(db.Model):
    """Sentences that make up each Quiz."""

    __tablename__ = "quiz_sentences"

    quiz_sentence_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.quiz_id'), nullable=False)
    sentence_id = db.Column(db.Integer, db.ForeignKey('sentences.sentence_id'), nullable=False)

    quiz = db.relationship('Quiz', backref='quiz_sentences')
    sentence = db.relationship('Sentence', backref='quiz_sentences')

    def __repr__(self):
        return f'<User quiz_sentence_id={self.quiz_sentence_id} quiz_id={self.quiz_id} sentence_id={self.sentence_id}>'


class Verb(db.Model):
    """Verbs to select from."""

    __tablename__ = "verbs"

    verb_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    verb = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<User verb_id={self.verb_id} verb={self.verb}>'


class Tense(db.Model):
    """Tenses to select from."""

    __tablename__ = "tenses"

    tense_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    tense = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<User tense_id={self.tense_id} tense={self.tense}>'


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

    def __repr__(self):
        return f'<User conjugated_verb_id={self.conjugated_verb_id} conjugated_verb={self.conjugated_verb} verb_id={self.verb_id} tense_id={self.tense_id} subject_pronoun={self.subject_pronoun}>'


class Sentence(db.Model): 
    """Sentences that the User gets answer in Quiz_Sentences."""

    __tablename__ = "sentences"

    sentence_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    blank_word_sentence = db.Column(db.Text, nullable=False)
    conjugated_verb_id = db.Column(db.Integer, db.ForeignKey('conjugated_verbs.conjugated_verb_id'), nullable=False)

    conjugated_verb = db.relationship('Conjugated_Verb', backref='sentences')

    def __repr__(self):
        return f'<User sentence_id={self.sentence_id} blank_word_sentence={self.blank_word_sentence} conjugated_verb_id={self.conjugated_verb_id}>'


def connect_to_db(flask_app, db_uri='postgresql:///wtf', echo=False):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app
    connect_to_db(app)