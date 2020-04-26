from list import db

data = db.execute("SELECT * FROM flights").fetchall()
print(data)
