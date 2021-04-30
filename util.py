import sqlite3

db = sqlite3.connect('blog.db')
c = db.cursor()

c.execute("""CREATE TABLE requests(
    name text,
    email text,
    subject text,
    description text
)""")
db.commit()
db.close()