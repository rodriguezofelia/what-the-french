"""CRUD operations."""

from model import db, User, Grade, Quiz, Quiz_Sentence, Verb, Tense, Conjugated_Verb, Sentence 

def create_user(email, first_name, last_name, created_at, modified_at, password):
    """Create and return a new user."""

    user = User(email=email, first_name=first_name, last_name=last_name, created_at=created_at, modified_at=modified_at, password=password)

    db.session.add(user)
    db.session.commit()

    return user

