import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine(os.getenv("DATABASE_URL"))
# dialect+driver://username:password@host:port/database
engine = create_engine("postgresql://postgres:admin%40123@localhost/lecture3")
db = scoped_session(sessionmaker(bind=engine))


def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    # print(reader)
    for id, origin, destination, duration in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES(:origin, :destination, :duration)", {"origin": origin, "destination": destination, "duration": duration})
        print(f"Added flights from {origin} to {destination} lasting {duration}")
        db.commit()


if __name__ == "__main__":
    main()
