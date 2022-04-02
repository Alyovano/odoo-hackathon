from flask import Flask, render_template

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
