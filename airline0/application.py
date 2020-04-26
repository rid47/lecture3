import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgresql://postgres:admin%40123@localhost/lecture3")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html", flights=flights)


@app.route("/booking", methods=["POST"])
def book():
    """Book a flight."""
    name = request.form.get("name")
    print(f"inserted name is {name}")
    try:
        flight_id = int(request.form.get("flight_id"))
        print(f"flight id is {flight_id}")
    except ValueError:
        return render_template("error.html", message="Invalid flight Number!")

    if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
        render_template("error.html", message="No such flight with that id.")
    else:
        db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)", {"name": name, "flight_id": flight_id})
        db.commit()
        return render_template("success.html")


@app.route("/flights")
def flights():
    """List all flights"""
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("flights.html", flights=flights)


@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details about a flight."""
    flight = db.execute("SELECT * FROM flights WHERE id = :id", {"id":flight_id}).fetchone()
    if flight is None:
        return render_template("error.html", message="No such flight.")

    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id", {"flight_id": flight_id}).fetchall()
    return render_template("flight.html", flight=flight, passengers=passengers)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port="8000")
