from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
app.count = 0
@app.route("/")
def index():
    app.count += 1
    print app.count
    return render_template("index.html", count=app.count)
@app.route("/add", methods=["POST"])
def add():
    app.count += 1
    print app.count
    return redirect("/")
@app.route("/clear", methods=["POST"])
def clear():
    app.count = -1
    return redirect("/")
app.run(debug=True)