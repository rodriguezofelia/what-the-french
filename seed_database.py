"""Script to seed database."""

import os
import json
from datetime import datetime

import crud
import model
import server

os.system('dropdb wtf')
os.system('createdb wtf')

model.connect_to_db(server.app)
model.db.create_all()

# with open('data/users.json') as f: 
#     user_data = json.loads(f.read())

# for user_record in user_data:
#     user = crud.create_user(user_record["email"], user_record["first_name"], 
#             user_record["last_name"], user_record["password"])


with open('data/quiz.json') as f:
    quiz_data = json.loads(f.read())

for quiz in quiz_data: 
    tense = crud.create_tense(quiz["tense"])
    verb = crud.create_verb(quiz["verb"])
    quiz_name = crud.create_quiz(quiz["quiz_name"], verb, tense)

    for sentence in quiz["sentences"]:
        conjugated_verb = crud.create_conjugated_verb(sentence["conjugated_verb"]["verb"], 
                verb.verb_id, tense.tense_id, sentence["conjugated_verb"]["subject_pronoun"])
        print(conjugated_verb)
        blank_word_sentence = crud.create_blank_word_sentence(sentence["blank_word_sentence"], 
                conjugated_verb)

        quiz_sentences = crud.add_quiz_sentences(quiz_name, blank_word_sentence)


# with open('data/grades.json') as f:
#     grade_data = json.loads(f.read())

# for grade_record in grade_data:
#     user_grade = crud.create_grade(grade_record["grade"], grade_record["uuid_code"], grade_record["user"], grade_record["quiz"])
