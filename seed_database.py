"""Script to seed database."""

import os
import json
from datetime import datatime

import crud
import model
import server

os.system('dropdb wtf')
os.system('createdb wtf')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/quiz.json') as f:
    quiz_data = json.loads(f.read())




# create quizzes with sentences and answer references

# create random set of users with emails and pws

# create a random set of grades for users