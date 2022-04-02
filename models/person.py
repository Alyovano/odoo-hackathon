import app

db = app.db

class Person(db.Model):
	id 			= db.Column('person_id', db.Integer, primary_key = True)
	lastname 	= db.Column(db.String(100))
	firstname	= db.Column(db.String(100))
	person_type = db.Column(db.String(100))
	email		= db.Column(db.String(100))
	phone		= db.Column(db.String(100))
	passwords 	= db.Column(db.String(100))