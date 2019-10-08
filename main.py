from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from contact import Contact

app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/index')
def index():
    if 'is_sent' in request.args:
        show_msg = True
        msg = "Your contact has been added!"
    elif 'is_deleted' in request.args:
        show_msg = True
        msg = "Your contact has been removed!"
    elif "is_edited" in request.args:
        show_msg = True
        msg = "Your contact has been updated!"
    else:
        show_msg = False
        msg = ""

    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()

    c.execute("SELECT * FROM contacts ORDER BY first")

    rows = c.fetchall()
    contacts = []

    for row in rows:
        c = Contact(row[1], row[2], row[3], id=row[0])
        contacts.append(c)

    return render_template('index.html', contacts=contacts, show_msg=show_msg, msg=msg)


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/form_data", methods=['POST'])
def form_data():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()

    if "id" in request.form:
        c1 = Contact(request.form['first'], request.form['last'], request.form['number'], id=request.form['id'])
        c.execute("""
            UPDATE contacts
            SET first = :first, last = :last, number = :number
            WHERE id = :id
        """, {"first": c1.first, "last": c1.last, "number" :c1.number, "id": c1.id})
        conn.commit()
        conn.close()
        return redirect(url_for('index', is_edited=True))
    else:
        # request.form will bring us the dictionary that the browser has created and sent
        c1 = Contact(request.form['first'], request.form['last'], request.form['number'])

        c.execute("""INSERT INTO contacts VALUES(:id,:f,:l,:num)""",
                  {"id": c1.id, "f": c1.first, "l": c1.last, "num": c1.number})

        conn.commit()
        conn.close()

        return redirect(url_for('index', is_sent=True))


@app.route("/delete/<id>")
def delete_contact(id):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("""DELETE FROM contacts WHERE id=:id""", {"id": id})
    conn.commit()
    conn.close()

    return redirect(url_for('index', is_deleted=True))


@app.route('/editContact/<id>')
def edit_contact(id):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()

    c.execute("""SELECT * FROM contacts WHERE id=:id""", {"id": id})
    row = c.fetchone()
    c1 = Contact(row[1], row[2], row[3], row[0])
    conn.close()
    return render_template('editContact.html', contact=c1)


@app.route("/search", methods=['POST'])
def search():
    name = request.form['first']
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM contacts WHERE lower(first) = lower(:name)""", {"name": name})
    rows = c.fetchall()
    contacts = []
    for row in rows:
        c = Contact(row[1], row[2], row[3], id=row[0])
        contacts.append(c)

    return render_template('index.html', contacts=contacts)




if __name__ == '__main__':
    app.run()