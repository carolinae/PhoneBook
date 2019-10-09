import sqlite3

conn = sqlite3.connect('mydb.db')
c = conn.cursor()

c.execute("""CREATE TABLE contacts(
            id text, first text, last text, number text
)""")

conn.commit()

conn.close()
