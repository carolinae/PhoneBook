import sqlite3

from contact import Contact

conn = sqlite3.connect('mydb.db')
c = conn.cursor()

# c.execute("""CREATE TABLE contacts(
#             id text, first text, last text, number text
# )""")

c1 = Contact("Carolina", "estrakh", "054-7422186")
c2 = Contact("amit", "yossefy", "0524338020")
c3 = Contact("yossef", "yossefy", "0522519101")
c4 = Contact("ime", "dede", "0524338010")

c.execute("""INSERT INTO contacts VALUES(:id,:f,:l,:num)""",{"id":c1.id, "f":c1.first, "l": c1.last, "num":c1.number})
c.execute("""INSERT INTO contacts VALUES(:id,:f,:l,:num)""",{"id":c2.id, "f":c2.first, "l": c2.last, "num":c2.number})
c.execute("""INSERT INTO contacts VALUES(:id,:f,:l,:num)""",{"id":c3.id, "f":c3.first, "l": c3.last, "num":c3.number})
c.execute("""INSERT INTO contacts VALUES(:id,:f,:l,:num)""",{"id":c4.id, "f":c4.first, "l": c4.last, "num":c4.number})

conn.commit()

conn.close()