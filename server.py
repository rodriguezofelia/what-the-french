

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
# app.secret_key = "dev"

@app.route('/')
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route('/quiz')
def all_quizzes():
    """View all verb and tense quiz options."""

    return render_template("word_conjugation.html")


@app.route('/podcasts')
def get_french_podcasts():
    """View French podcast options from API."""

    return render_template("podcasts.html")


@app.route('/users/<user_id>')
def show_user_profile(user_id):

    user = crud.get_user_by_id(user_id)

    return render_template('user_profile.html', user=user)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

