

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"

@app.route('/')
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route('/word-conjugation')
def quiz_selection():
    """View all verb and tense quiz options."""

    verbs = crud.get_verbs()
    tenses = crud.get_tenses()

    return render_template("word_conjugation.html", verbs=verbs, tenses=tenses)

@app.route('/quiz', methods=['POST'])
def quiz():
    """Take quiz."""

    verb_id = request.form.get('verb_id')
    tense_id = request.form.get('tense_id')

    quiz = crud.get_quiz_by_verb_and_tense(verb_id, tense_id)
    sentences = quiz.sentences

    return render_template("quiz.html", quiz=quiz, sentences=sentences)

@app.route('/podcasts')
def get_french_podcasts():
    """View French podcast options from API."""

    return render_template("podcasts.html")


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
        session['user'] = user.user_id
        flash('You have been logged in!')
        return redirect('/users/' + str(user.user_id))
        
    else:
        flash('Oh no! Try again.')


@app.route('/users/<user_id>')
def show_user_profile(user_id):
    
    user = crud.get_user_by_id(user_id)
    all_grades = crud.get_grade_by_id(user_id)
    quiz_names = crud.get_quiz_name_by_user_id(user_id)

    return render_template('user_profile.html', user=user, all_grades=all_grades, quiz_names=quiz_names)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

