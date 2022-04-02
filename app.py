from enum import auto
from flask import Flask, render_template
import sqlalchemy as db

"""
#### STRUCTURE DATABASES
"""
engine = db.create_engine('sqlite:///app.db')
connection = engine.connect()
metadata = db.MetaData()

person = db.Table('person', metadata, autoload=True, autoload_with=engine)


"""
#### END
"""

api = Flask(__name__)

"""###
###### Home + API
###"""

@api.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@api.route('/events', methods=['GET'])
def get_events():
    return {'event': 'hello'}

if __name__ == '__main__':
    api.run() 
