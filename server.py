from flask import Flask, json
import sqlite3

api = Flask(__name__)
db = sqlite3.connect('app.db')
cursor = db.cursor()

"""###
###### Database Creation
###"""

table_events = """CREATE TABLE IF NOT EXISTS events (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT
)"""

cursor.execute(table_events)



db.commit()

"""###
###### End Database Creation
###"""

@api.route('/', methods=['GET'])
def get_index():
    return 

if __name__ == '__main__':
    api.run() 
