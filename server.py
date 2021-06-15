

from flask import (Flask, render_template, request, session,
                   redirect, jsonify, make_response)
from flask_api import status
from model import connect_to_db
import crud
import uuid
import json
import bcrypt
import requests
import base64
import config


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

    decoded_request = json.loads(request.data)
    email = decoded_request['email']
    password = decoded_request['password']
    first_name = decoded_request['first_name']
    last_name = decoded_request['last_name']
    duplicate_email_msg = "This email is already taken. Sign in with the account associated with this email or create a new account. "

    user = crud.get_user_by_email(email)

    if user:
        response = jsonify({"error": duplicate_email_msg,}), status.HTTP_400_BAD_REQUEST
        return response
    else: 
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = crud.create_user(email, first_name, last_name, hashed_pw)
        session["user"] = user.user_id
        response = make_response({}, 200)
        response.set_cookie("logged-in", "true")
        return response


@app.route('/login', methods=['POST'])
def set_cookie():
    """Sets cookie if user exists and passes status."""

    decoded_request = json.loads(request.data)
    email = decoded_request['email']
    password = decoded_request['password']
    incorrect_pw_msg = 'Oh no, this does not look like its correct. Please try again.'

    user = crud.get_user_by_email(email)
    correct_password = crud.is_correct_password(email, password)

    if correct_password:
        session["user"] = user.user_id
        response = make_response({}, 200)
        response.set_cookie("logged-in", "true")
        return response
    
    else:
        response = jsonify({"error": incorrect_pw_msg}), status.HTTP_400_BAD_REQUEST
        return response


@app.route('/profile')
def show_user_profile():
    
    user_id = session.get('user')

    if not user_id:
        return redirect('/')
    
    user = crud.get_user_by_id(user_id)
    all_grades = crud.get_grade_by_id(user_id)
    quiz_names = crud.get_quiz_name_by_user_id(user_id)
    
    return render_template('user-profile.html', user=user, all_grades=all_grades, quiz_names=quiz_names)



@app.route('/verb-conjugation')
def quiz_selection():
    """View all verb and tense quiz options."""

    verbs = crud.get_verbs()
    tenses = crud.get_tenses()

    return render_template("verb-conjugation.html", verbs=verbs, tenses=tenses)


@app.route('/quiz', methods=['POST'])
def quiz():
    """Take quiz."""

    verb = request.form.get('verb')
    tense = request.form.get('tense')

    print(verb, "verb")
    print(tense, "tense")
    if verb and tense: 
        quiz = crud.get_quiz_by_verb_and_tense(verb, tense)
        sentences = crud.get_quiz_sentences(quiz.quiz_id)
        quiz_name = crud.get_quiz_name_by_id(quiz.quiz_id)
        uuid_code = uuid.uuid4()

        return render_template("quiz.html", quiz=quiz, uuid_code=uuid_code, sentences=sentences, quiz_name=quiz_name)
    else: 
        return redirect('/verb-conjugation')

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


@app.route('/sign-in')
def sign_in():
    """Renders login form."""

    return render_template("login.html")

@app.route('/sign-up')
def sign_up():
    """Log into account."""

    return render_template("sign-up.html")

@app.route('/sign-out')
def sign_out():
    """Log user out of account."""

    session.clear()
    response = make_response(redirect('/'))
    response.delete_cookie("logged-in")
    return response

@app.route('/spotify-auth')
def french_podcasts():

    secret_str = config.spotify_client_id + ":" + config.spotify_client_secret
    secret_bytes = base64.b64encode(secret_str.encode('utf-8'))

    auth_response = requests.post('https://accounts.spotify.com/api/token?grant_type=client_credentials', 
        headers={'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic ' + secret_bytes.decode('utf-8') })

    access_token = auth_response.json()['access_token']

    search_api_response = requests.get('https://api.spotify.com/v1/search?q=french%10podcasts&type=playlist', 
        headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token})
    
    dict_search_api_res = dict(search_api_response.json())
    return dict_search_api_res


if __name__ == '__main__': 
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

