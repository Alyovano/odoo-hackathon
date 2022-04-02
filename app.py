from flask import Flask, render_template
from database import Database

api = Flask(__name__)

db = Database()

@api.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@api.route('/admin', methods=['GET'])
def admin():
    return render_template('admin/index.html')

@api.route('/calendar', methods=['GET'])
def get_events():
    # Chercher en db les events
    return render_template('calendar.html')

@api.route('/cursusflix', methods=['GET'])
def get_cursusflix():
    # Chercher en db les events
    return render_template('cursusflix.html')


@api.route('/courses', methods=['GET'])
def get_courses():
    # Chercher en db les events
    return render_template('courses.html')
if __name__ == '__main__':
    api.run() 
