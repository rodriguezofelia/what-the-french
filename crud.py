"""CRUD operations."""

from model import db, User, Grade, Quiz, Quiz_Sentence, Verb, Tense, Conjugated_Verb, Sentence, connect_to_db 

def create_user(email, first_name, last_name, password):
    """Create and return a new user."""

    user = User(email=email, first_name=first_name, last_name=last_name, password=password)

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
    

def get_grade_by_id(user_id):
    """Return all grades for user."""

    return Grade.query.filter(Grade.user_id == user_id).all()


def get_user_by_id(user_id):
    """Return all users by ID."""

    return User.query.get(user_id)

    
def get_quiz_name_by_user_id(user_id):
    """Return quiz by quiz name by filtering by user ID."""
    
    quiz_name = db.session.query(Quiz.quiz_name, Grade.grade, Grade.user_id, Quiz.quiz_id).join(Quiz).filter(Grade.user_id == user_id).all()

    return quiz_name


def get_user_by_email(email):
    """Return user if email exists."""

    return User.query.filter(User.email == email).first()

def is_correct_password(email, password):

    user = get_user_by_email(email)

    if user != None:
        return user.password == password

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    