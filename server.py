

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
import uuid

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"

@app.route('/')
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""

    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    user = crud.get_user_by_email(email)

    if user:
        flash('This account is already taken. Sign in with the account associated with this email or create a new account.')

    else: 
        user = crud.create_user(email, first_name, last_name, password)
    
    return redirect('/')


@app.route('/login', methods=['POST'])
def login_user():
    """Logs in a user to user profile."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    correct_password = crud.is_correct_password(email, password)

    if correct_password:
        session["user"] = user.user_id
        return redirect('/profile')
    
    else:
        flash('Oh no! Try again.')
        return redirect('/')


@app.route('/profile')
def show_user_profile():
    
    user_id = session.get('user')

    if not user_id:
        return redirect('/')
    
    user = crud.get_user_by_id(user_id)
    all_grades = crud.get_grade_by_id(user_id)
    quiz_names = crud.get_quiz_name_by_user_id(user_id)
    
    return render_template('user_profile.html', user=user, all_grades=all_grades, quiz_names=quiz_names)



@app.route('/word-conjugation')
def quiz_selection():
    """View all verb and tense quiz options."""

    user_id = session.get('user')

    if not user_id:
        flash("You must be signed in to take a quiz.")
        return redirect('/')

    verbs = crud.get_verbs()
    tenses = crud.get_tenses()

    return render_template("word_conjugation.html", verbs=verbs, tenses=tenses)


@app.route('/quiz', methods=['POST'])
def quiz():
    """Take quiz."""

    verb = request.form.get('verb')
    tense = request.form.get('tense')

    quiz = crud.get_quiz_by_verb_and_tense(verb, tense)
    sentences = crud.get_quiz_sentences(quiz.quiz_id)
    quiz_name = crud.get_quiz_name_by_id(quiz.quiz_id)
    uuid_code = uuid.uuid4()

    if verb and tense: 
        return render_template("quiz.html", quiz=quiz, uuid_code=uuid_code, sentences=sentences, quiz_name=quiz_name)
    else: 
        flash("You must select a verb and tense to proceed.")
        return redirect('/word-conjugation')

@app.route('/grade', methods=['POST'])
def quiz_grade():
    """Grade for quiz."""

    user_id = session.get('user')
    quiz_id = request.form.get('quiz_id')
    uuid_code = request.form.get('uuid')
    quiz_name = crud.get_quiz_name_by_id(quiz_id)
    sentences = crud.get_quiz_sentences(quiz_id)

    answers = {}
    num_correct_answers = 0
    num_questions = len(sentences)

    for sentence in sentences:
        user_answer = request.form.get('answer_' + str(sentence.sentence_id))
        sentence_id = sentence.sentence_id
        sentence_answer = crud.get_sentence_answer(sentence_id)
        
        answers[sentence_id] = [user_answer.lower(), sentence_answer[0].lower(), user_answer.lower() == sentence_answer[0]]


        if user_answer.lower() == sentence_answer[0]:
            num_correct_answers += 1

    score = (num_correct_answers/num_questions) * 100

    if not crud.get_grade_by_uuid(uuid_code, user_id, quiz_id): 
        crud.insert_grade(score, uuid_code, user_id, quiz_id)
        
    return render_template("grade.html", quiz_id=quiz_id, sentences=sentences, quiz_name=quiz_name, answers=answers, score=score)       


@app.route('/podcasts')
def get_french_podcasts():
    """View French podcast options from API."""

    return render_template("podcasts.html")


if __name__ == '__main__': 
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

