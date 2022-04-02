from flask import Flask, render_template
from database import Database
import json
api = Flask(__name__)

NULL = 0

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
    with open('data/course_bank.json') as f:
        data = json.load(f)
    print(data)
    return render_template('cursusflix.html', content=data)

@api.route('/courses', methods=['GET'])
def get_courses():
    return render_template('courses.html')

@api.route('/profile', methods=['GET'])
def get_profile():
	# data = []
	# cursor = db.cursor()
	# cursor.execute('SELECT * FROM person')
	# rows = cursor.fetchall()
	# Peut etre pas obligatoire
	# for row in rows:
	# 	data.append(row)
	# print(data)
	return render_template('profile.html')


# =================================================================
# ------------------- --- ENDPOINTS EVENT --- ---------------------
# =================================================================
@api.route('/calendar/events/list/all')
def get_all_events():
    return {
		"id": 1,
		"view_group": "admin",
		"ownerId": 1,
		"allDay": 0,
		"start": "2022-04-02 10:00:00",
		"startStr": "",
		"end": "2022-04-02 20:00:00",
		"endStr": "",
		"title": "Fbqzfbqlzkbc",
		"url": "http://localhost:8080/calendar/event/view?id=1",
		"editable": NULL,
		"startEditable": NULL,
		"durationEditable": NULL,
		"resourceEditable": NULL,
		"display": "auto",
		"overlap": NULL,
		"constraint": "",
		"backgroundColor": "#000000",
		"borderColor": "#000000",
		"textColor": "#000000",
		"source": "http://localhost:8080/calendar/event/getevent?id=1"
	}

if __name__ == '__main__':
    api.run() 
