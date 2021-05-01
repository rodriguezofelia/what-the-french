"""CRUD operations."""

from model import db, User, Grade, Quiz, Quiz_Sentence, Verb, Tense, Conjugated_Verb, Sentence, connect_to_db 

def create_user(email, first_name, last_name, created_at, modified_at, password):
    """Create and return a new user."""

    user = User(email=email, first_name=first_name, last_name=last_name, created_at=created_at, modified_at=modified_at, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_grade(created_at, grade, user, quiz):
    """Create and return a new quiz grade."""

    grade = Grade(created_at=create_at, grade=grade, user=user, quiz=quiz)

    db.session.add(grade)
    db.session.commit()

    return grade

def create_quiz(quiz_name, verb, tense):
    """Create and return a new quiz."""

    quiz = Quiz(quiz_name=quiz_name, verb=verb, tense=tense)

    db.session.add(quiz)
    db.session.commit()

    return quiz
    

def get_grade_by_id(grade_id):
    """Return all grades for user by ID."""

    return Grade.query.all(grade_id)


def get_user_by_id(user_id):
    """Return all users by ID."""

    return User.query.get(user_id)

    
