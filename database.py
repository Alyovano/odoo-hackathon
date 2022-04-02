import sqlite3

class Database():
    def __init__(self):
        self.db = sqlite3.connect('app.db')
        self.init_database()

    def init_database(self):
        sql = """CREATE TABLE IF NOT EXISTS events (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
date_start INTEGER,
date_stop INTEGER
)"""

        cursor = self.db.cursor()
        cursor.execute(sql)




        self.db.commit()
