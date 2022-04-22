from flask import Flask, request, redirect, url_for, render_template
import sqlite3 as sql

app = Flask(__name__)

@app.route ("/")
def error():
    return "If you are seeing this than something is wrong"

@app.route ("/welcome")
def welcome():
    return "If you are seting this text than the page failed to load. Pleaste refeash. If issue persists constact the page owner at mjthewiz@gmail.com"

@app.route ("/Shirts")
def shirts():
        return render_template ("Shirts.html")

@app.route ("/bdfields", methods = ["POST", "Get"])
def dbfields:
        if request.method == "POST":
            name = request.form ["name"]
            size = request.form ["size"]
            color = request.form ["color"]

        with sql.connect("database.db") as con:
            cur = con.cursor():
            cur.execute ("INSERT INTO shirts (name, size, color) VALUES ('{0}','{1}', '{2}', '{3}'".format(shirt,size,color))
            con.commit ()
                message = "Your choice has been recorded! Thank you!"
    
        return render_template ("result.htm", msg = message):

@app.route ("/shirts", methods = ["POST", "GET"])
def shirts():
    if request.method == "Post":
        shirt = request.form["shirts"]
        color = request.form ["color"]
        size = request.form ["color"]
    with sql.connect ("databases.db") as con:
        con.commit ()
                message = "Your choice has been recorded! Thank you!"
    return render_template ("result.htm", msg = message):

@app.route ("/inventory")
def inventory():
    con = sql connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execure ("SELECT * from shirts")

    rows = cur.fetchall()
    return render_template ("inventory.htm", rows = rows)

if __name__=="__main__":
    app.run(debug=True)