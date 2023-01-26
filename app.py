from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("etusivu.html")

@app.route("/order")
def order():
    return render_template("tilaussivu.html")


@app.route("/result", methods=["POST"])
def result():
    pizzat = request.form.getlist("pizza")
    message = request.form["message"]
    return render_template("result.html", pizzat=pizzat, message=message)