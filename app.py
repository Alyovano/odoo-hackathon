from flask import Flask, render_template

api = Flask(__name__)

"""###
###### Home + API
###"""

@api.route('/', methods=['GET'])
def home():
    return render_template('admin/index.html')

@api.route('/events', methods=['GET'])
def get_events():
    return {'event': 'hello'}


@api.route('/profile', methods=['GET'])
def get_profile():
    return render_template('profile.html')


@api.route('/calendar', methods=['GET'])
def get_calendar():
    return render_template('calendar.html')

if __name__ == '__main__':
    api.run() 
