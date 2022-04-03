from flask import Flask, redirect, render_template, jsonify, request
from database import Database
import json
import datetime

api = Flask(__name__)

NULL = 0

database = Database()
db = database.db


@api.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@api.route("/admin", methods=["GET"])
def admin():
    return render_template("admin/index.html")


@api.route("/calendar", methods=["GET"])
def get_events():
    # Chercher en db les events
    cursor = db.cursor()
    cursor.execute("SELECT * FROM events")
    rows = cursor.fetchall()
    events = []
    [
        events.append(
            {
                "event_id": rows[i][0],
                "title": rows[i][1],
                "start": rows[i][2],
                "end": rows[i][3],
                "description": rows[i][5],
            }
        )
        for i in range(len(rows))
    ]
    print(events)
    return render_template("calendar.html", events=events)


@api.route("/calendar/event/<int:id>")
def get_event(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM events WHERE event_id = {}".format(id))
    rows = cursor.fetchall()
    event = rows
    cursor.execute("SELECT * FROM event_attendes WHERE event_id = {}".format(id))
    rows = cursor.fetchall()
    person_attendes = rows
    persons = []
    for i in range(len(person_attendes)):
        cursor.execute(
            "SELECT * FROM person WHERE person_id = {}".format(person_attendes[i][2])
        )
        rows = cursor.fetchall()
        persons.append(
            {
                "id": rows[0][0],
                "lastname": rows[0][1],
                "firstname": rows[0][2],
                "person_type": rows[0][3],
                "email": rows[0][4],
            }
        )
    return render_template(
        "view_event.html",
        event={
            "event_id": event[0][0],
            "title": event[0][1],
            "start": event[0][2],
            "end": event[0][3],
            "organizer": event[0][4],
            "description": event[0][5],
            "category_id": event[0][6],
        },
        persons=persons,
    )


@api.route("/calendar/event/create", methods=["POST"])
def create_event():
    data = request.form
    start = data.get("start")
    end = data.get("end")
    cursor = db.cursor()
    cursor.execute(
        """INSERT INTO events
                    ("title", "date_from", "date_to", "organizer", "event_description", "category_id")
                    VALUES ('TITLE', '{}', '{}', 1, 'Description', 1);
                """.format(
            start, end
        )
    )
    db.commit()
    return True


@api.route("/calendar/event/update/form", methods=["POST"])
def update_event_form():
    data = request.form
    cursor = db.cursor()
    cursor.execute(
        """UPDATE events SET date_from = \'{}\', date_to = \'{}\', title = \'{}\', title = \'{}\', event_description = \'{}\' WHERE event_id = {}""".format(
            data.get("date_from"),
            data.get("date_to"),
            data.get("title"),
            data.get("description"),
            data.get("id"),
        )
    )
    db.commit()
    return redirect("/calendar/event/{}".format(data.get("id")))


@api.route("/calendar/event/update/drop", methods=["POST"])
def update_event_drop():
    data = request.form
    start = data.get("start")
    end = data.get("end")
    cursor = db.cursor()
    cursor.execute(
        """UPDATE events SET date_from = \'{}\', date_to = \'{}\' WHERE event_id = {}""".format(
            start, end, data.get("event_id")
        )
    )
    db.commit()
    return redirect("/calendar/event/{}".format(data.get("event_id")))


@api.route("/cursusflix", methods=["GET"])
def get_cursusflix():
    with open("data/course_bank.json") as f:
        data = json.load(f)
    print(data)
    return render_template("cursusflix.html", content=data)


@api.route("/cursusflix/<string:course_name>", methods=["GET"])
def get_cursusflix_ressources(course_name):
    print(course_name)
    return "<h1>hello</h1>"


@api.route("/courses", methods=["GET"])
def get_courses():
    return render_template("courses.html")


@api.route("/profile", methods=["GET"])
def get_profile():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM person WHERE person_id=1;")
    rows = cursor.fetchall()
    profil_exemple = {
        "id": rows[0][0],
        "lastname": rows[0][1],
        "firstname": rows[0][2],
        "person_type": rows[0][3],
        "email": rows[0][4],
    }
    print(profil_exemple)
    return render_template("profile.html", content=profil_exemple)


if __name__ == "__main__":
    api.run()
