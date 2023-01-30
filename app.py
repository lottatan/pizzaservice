from flask import Flask
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import users

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///user"
db = SQLAlchemy(app)

app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    k = db.session.execute("SELECT comment FROM comments")
    kommentit = k.fetchall()
    return render_template("etusivu.html", kommentit=kommentit)

@app.route("/order")
def order():
    return render_template("tilaussivu.html")


@app.route("/result", methods=["POST"])
def result():
    pizzat = request.form.getlist("pizza")
    message = request.form["message"]
    return render_template("result.html", pizzat=pizzat, message=message)

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # TODO: check username and password
    session["username"] = username
    return redirect("/")

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("create.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

    if users.create(username, password):
        return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")