import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine(os.getenv("DATABASE_URL"))
# dialect+driver://username:password@host:port/database
engine = create_engine("postgresql://postgres:admin%40123@localhost/lecture3")
db = scoped_session(sessionmaker(bind=engine))


def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration}")


if __name__ == "__main__":
    main()
