from flask import Flask, render_template, jsonify
from database import Database
import json
import datetime
api = Flask(__name__)

NULL = 0

database = Database()
db = database.db

@api.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@api.route('/admin', methods=['GET'])
def admin():
    return render_template('admin/index.html')

@api.route('/calendar', methods=['GET'])
def get_events():
    # Chercher en db les events
    cursor = db.cursor()
    cursor.execute('SELECT * FROM events')
    rows = cursor.fetchall()
    events = []
    [events.append({'title': rows[i][1], 'start': rows[i][2], 'end': rows[i][3]}) for i in range(len(rows))]
    print(events)
    return render_template('calendar.html', events=events)

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
	data = []
	cursor = db.cursor()
	cursor.execute('SELECT * FROM person WHERE person_id=1;')
	rows = cursor.fetchall()
	profil_exemple = {
		'id': rows[0][0],
		'lastname': rows[0][1],
		'firstname': rows[0][2],
		'person_type': rows[0][3],
		'email': rows[0][4],
	}
	print(profil_exemple)
	return render_template('profile.html', content=profil_exemple)


# =================================================================
# ------------------- --- ENDPOINTS EVENT --- ---------------------
# =================================================================
@api.route('/calendar/events/list/all')
def get_all_events():
	return {'events': [{
		'title': 'Hello',
		'start': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
		'end': (datetime.datetime.now() + datetime.timedelta(hours=2)).strftime('%Y-%m-%d %H:%M:%S')
	}]}
    #return jsonify({
	#	"id": 1,
	#	"view_group": "admin",
	#	"ownerId": 1,
	#	"allDay": 0,
	#	"start": "2022-04-02 10:00:00",
	#	"end": "2022-04-02 20:00:00",
	#	"title": "Fbqzfbqlzkbc",
	#	"url": "http://localhost:8080/calendar/event/view?id=1",
	#	"editable": NULL,
	#	"startEditable": NULL,
	#	"durationEditable": NULL,
	#	"resourceEditable": NULL,
	#	"display": "auto",
	#	"overlap": NULL,
	#	"constraint": "",
	#	"backgroundColor": "#000000",
	#	"borderColor": "#000000",
	#	"textColor": "#000000",
	#	"source": "http://localhost:8080/calendar/event/getevent?id=1"
	#})

if __name__ == '__main__':
    api.run() 
