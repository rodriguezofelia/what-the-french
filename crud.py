"""CRUD operations."""

from model import db, User, Grade, Quiz, Quiz_Sentence, Verb, Tense, Conjugated_Verb, Sentence, connect_to_db
import bcrypt 

def create_user(email, first_name, last_name, password):
    """Create and return a new user."""

    user = User(email=email, first_name=first_name, last_name=last_name, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_grade(grade, uuid_code, user_id, quiz_id):
    """Create and return a new quiz grade."""

    user_grade = Grade(grade=grade, uuid_code=uuid_code, user_id=user_id, quiz_id=quiz_id)

    db.session.add(user_grade)
    db.session.commit()

    return user_grade

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
        return bcrypt.checkpw(password.encode('utf8'), user.password)

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

    return Quiz.query.filter(Quiz.verb_id == verb_id).filter(Quiz.tense_id == tense_id).first()

def get_quiz_sentences(quiz_id):
    """Return the sentences that belong to given quiz id."""

    sentences = Quiz.query.get(quiz_id).sentences

    return sentences

def get_quiz_name_by_id(quiz_id):
    """Return the quiz name by quiz id."""

    quiz_name = Quiz.query.get(quiz_id).quiz_name

    return quiz_name

def get_sentence_answer(sentence_id):
    """Return the answer for given sentence."""

    sentence_answer = db.session.query(Conjugated_Verb.conjugated_verb).join(Sentence).filter(Sentence.sentence_id == sentence_id).one()

    return sentence_answer

def insert_grade(grade, uuid_code, user_id, quiz_id):
    """Insert quiz grade into Grades table."""

    new_grade = Grade(grade=grade, uuid_code=uuid_code, user_id=user_id, quiz_id=quiz_id)

    db.session.add(new_grade)
    db.session.commit()

def create_verb(verb):
    """Insert verbs into Verbs table."""

    existing_verb = Verb.query.filter_by(verb=verb).first()

    if existing_verb:
        return existing_verb

    verb = Verb(verb=verb)

    db.session.add(verb)
    db.session.commit()

    return verb

def create_tense(tense):
    """Insert verbs into Tense table."""

    existing_tense = Tense.query.filter_by(tense=tense).first()

    if existing_tense:
        return existing_tense

    tense = Tense(tense=tense)

    db.session.add(tense)
    db.session.commit()

    return tense

def create_blank_word_sentence(blank_word_sentence, conjugated_verb):
    """Insert blank word sentence into Sentence table."""

    blank_word_sentence = Sentence(blank_word_sentence=blank_word_sentence, conjugated_verb=conjugated_verb)

    db.session.add(blank_word_sentence)
    db.session.commit()

    return blank_word_sentence

def create_conjugated_verb(conjugated_verb, verb_id, tense_id, subject_pronoun):

    conjugated_verb = Conjugated_Verb(conjugated_verb=conjugated_verb, verb_id=verb_id, tense_id=tense_id, 
            subject_pronoun=subject_pronoun)

    db.session.add(conjugated_verb)
    db.session.commit()

    return conjugated_verb

def add_quiz_sentences(quiz, sentence):

    quiz.sentences.append(sentence)

    db.session.add(quiz)
    db.session.commit()

def get_grade_by_uuid(uuid_code, user_id, quiz_id):

    grade = Grade.query.filter_by(uuid_code=uuid_code, user_id=user_id, quiz_id=quiz_id).first()

    return grade

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    