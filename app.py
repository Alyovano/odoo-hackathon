from enum import auto
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

api = Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///app.db'
api.config['SECRET_KEY'] = 'RUSH B WINNER'
db = SQLAlchemy(api)



"""
#### STRUCTURE DATABASES
"""

class person(db.Model):
	id 			= db.Column('person_id', db.Integer, primary_key = True)
	lastname 	= db.Column(db.String(100))
	firstname	= db.Column(db.String(100))
	person_type = db.Column(db.String(100))


"""
#### END
"""

"""###
###### Home + API
###"""


@api.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@api.route('/events', methods=['GET'])
def get_events():
    return person.query.all()

if __name__ == '__main__':
    db.create_all()
    api.run(debug=True)
