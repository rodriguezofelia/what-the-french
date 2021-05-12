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
    """Return user by ID."""

    return User.query.filter(User.user_id == user_id).first()

    
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
        # return user.password == password

        return True

def get_verbs():
    """Return all verbs."""

    return Verb.query.all()

def get_tenses():
    """Return all tenses."""

    return Tense.query.all()

def get_quiz_by_id(quiz_id):
    """Return the quiz."""

    return Quiz.query.get(quiz_id)

def get_quiz_by_verb_and_tense(verb_id, tense_id):
    """Return the quiz for the given verb and tense."""

    return Quiz.query.filter(verb_id == verb_id).filter(tense_id == tense_id).first()

def get_quiz_sentences(quiz_id):
    """Return the sentences that belong to given quiz id."""

    sentences = Quiz.query.get(quiz_id).sentences

    return sentences

def get_quiz_name_by_id(quiz_id):
    """Return the quiz name by quiz id."""

    quiz_name = Quiz.query.get(quiz_id).quiz_name

    return quiz_name


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    