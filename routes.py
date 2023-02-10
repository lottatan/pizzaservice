from app import app
import users
import kommentit
from flask import render_template, request, redirect
from db import db
import orders

@app.route("/")
def index():
    return render_template("etusivu.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/profile")
        
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
            return redirect("/profile")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/comments")
def comments():
    kommentit1 = kommentit.get_list()
    rating = kommentit.get_average_rating()
    return render_template("comments.html", kommentit=kommentit1, rating=rating)

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "GET":
        return render_template("send.html")

    if request.method == "POST":
        # users.check_csrf()

        kommentti = request.form["kommentti"]
        if len(kommentti) > 100:
            return render_template("/error.html", message="Kommentti on liian pitkä")
        
        if kommentit.add_comment(kommentti):
            return render_template("profile.html")
        
@app.route("/rate", methods=["GET", "POST"])
def rate():
    if request.method == "GET":
        return render_template("profile.html")
    if request.method == "POST":
        # users.check_csrf()

        rating = request.form["rating"]
        if kommentit.add_rating(rating):
            return render_template("profile.html")
        
        return render_template("/error.html", message="Arvostelu ei onnistunut")

@app.route("/order")
def order():
    return render_template("tilaussivu.html")

@app.route("/result", methods=["POST"])
def result():
    pizzat = request.form.getlist("pizza")
    drinks = request.form.getlist("drink")
    message = request.form["message"]
    if orders.add_order(pizzat) and orders.add_drink_order(drinks):
        return render_template("result.html", pizzat=pizzat, message=message, drinks=drinks)
    else:
        return render_template("error.html", message="Tilaus ei onnistunut")
    
@app.route("/personal_stats")
def personal_stats():
    username = users.username()
    spent = orders.user_total_spending(username)
    list = orders.all_user_orders(username)
    favorite_pizza = orders.get_favorite_pizza(username)
    favorite_drink = orders.get_favorite_drink(username)
    return render_template("personal_stats.html", spent=spent, list=list, favorite_pizza=favorite_pizza, favorite_drink=favorite_drink)
