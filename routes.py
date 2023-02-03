from app import app
import users
import comments
from flask import render_template, request, redirect
from db import db

@app.route("/")
def index():
    return render_template("etusivu.html")

@app.route("/send", methods=["POST"])
def send():
    kommentti = request.form("kommentti")
    if comments.send(kommentti):
        return redirect("/")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

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
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("create.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if len(username) == 0:
            return render_template("error.html", message="Syötä käyttäjätunnus")
        if len(password) == 0:
            return render_template("error.html", message="Syötä salasana")
        if users.create(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/send", methods=["GET", "POST"])
def new():
    if request.method == "GET":
        return render_template("profile.html")

    if request.method == "POST":

        kommentti = request.form["kommentti"]

        if len(kommentti) > 100:
            return render_template("/error.html", message="Kommentti on liian pitkä")
        
        user = users.username()

        if user:
            comments.add_comment(user, kommentti)

@app.route("/comments")
def comments():
    kommentit = comments.get_list()
    return render_template("comments.html", kommentit=kommentit)