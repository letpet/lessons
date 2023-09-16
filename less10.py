import sqlite3

db = sqlite3.connect("database.sl3", 5)
cur = db.cursor()

# cur.execute("CREATE TABLE first_table (name Text);")
cur.execute("INSERT INTO first_table (name, age) VALUES ('Ann', 12);")

db.commit()
db.close()
