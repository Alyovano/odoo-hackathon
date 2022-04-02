from enum import auto
from unicodedata import name
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

api = Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
api.config['SECRET_KEY'] = 'RUSH B WINNER'

db = SQLAlchemy(api)

"""
#### STRUCTURE DATABASES
"""

# class Person(db.Model):
# 	id 			= db.Column('person_id', db.Integer, primary_key = True)
# 	lastname 	= db.Column(db.String(100))
# 	firstname	= db.Column(db.String(100))
# 	person_type = db.Column(db.String(100))
# 	email		= db.Column(db.String(100))
# 	phone		= db.Column(db.String(100))
# 	passwords 	= db.Column(db.String(100))

# class Category(db.Model):
#     id			= db.Column('category_id', db.Integer, primary_key = True)
#     name 		= db.Column(db.String(100))

# class Cours(db.Model):
#     id			= db.Column('cours_id', db.Integer, primary_key = True)
#     category_id = db.Column(db.Integer)
#     name		= db.Column(db.String(100))
#     level		= db.Column(db.Integer)
#     required	= db.Column(db.Integer)

# class CoursPerson(db.Model):
#     id			= db.Column('cours_person_id', db.Integer, primary_key = True)
#     person		= db.Column(db.Integer)
#     cours		= db.Column(db.Integer)

# class Event(db.Model):
#     id			= db.Column('event_id', db.Integer, primary_key = True)
#     title 		= db.Column(db.String(100))
#     date_from 	= db.Column(db.Integer)
#     date_to		= db.Column(db.Integer)
#     organizer 	= db.Column(db.Integer)

# class EventAttendes(db.Model):
#     id			= db.Column('event_attendes_id', db.Integer, primary_key = True)
#     event_id	= db.Column(db.Integer)
#     person_id	= db.Column(db.Integer)


"""
#### END
"""

"""###
###### Home + API
###"""

if __name__ == '__main__':
    api.run(debug=True)
