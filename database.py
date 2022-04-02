import sqlite3

class Database():
    def __init__(self):
        self.db = sqlite3.connect('app.db', isolation_level=None, check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self.init_database()

    def init_database(self):
        person = """CREATE TABLE IF NOT EXISTS person (
            person_id INTEGER NOT NULL, 
            lastname VARCHAR(100), 
            firstname VARCHAR(100), 
            person_type VARCHAR(100), 
            email VARCHAR(100), 
            phone VARCHAR(100), 
            passwords VARCHAR(100), 
            PRIMARY KEY (person_id)
        )"""
        cursor = self.db.cursor()
        cursor.execute(person)



        category = """CREATE TABLE IF NOT EXISTS category (
                        category_id INTEGER NOT NULL, 
                        name VARCHAR(100), 
                        PRIMARY KEY (category_id)
                    )"""
        cursor.execute(category)



        courses =   """CREATE TABLE IF NOT EXISTS courses (
                        cours_id INTEGER NOT NULL,
                        category_id INTEGER,
                        name VARCHAR(100),
                        level INTEGER,
                        required INTEGER, 
                        PRIMARY KEY (cours_id)
                    )"""
        cursor.execute(courses)
        
        
        
        cours_person = """CREATE TABLE IF NOT EXISTS cours_person (
                            cours_person_id INTEGER NOT NULL, 
                            person INTEGER, 
                            cours INTEGER, 
                            PRIMARY KEY (cours_person_id)
                        )"""
        cursor.execute(cours_person)



        events =    """CREATE TABLE IF NOT EXISTS events (
                        event_id INTEGER NOT NULL, 
                        title VARCHAR(100), 
                        date_from INTEGER, 
                        date_to INTEGER, 
                        organizer INTEGER, 
                        event_description TEXT,
                        PRIMARY KEY (event_id)
                    )"""
        cursor.execute(events)



        events_attended =   """CREATE TABLE IF NOT EXISTS event_attendes (
                                event_attendes_id INTEGER NOT NULL, 
                                event_id INTEGER, 
                                person_id INTEGER, 
                                PRIMARY KEY (event_attendes_id)
                            )"""
        cursor.execute(events_attended)
        self.db.commit()
