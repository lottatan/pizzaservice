from flask import session, request, abort
from db import db
from sqlalchemy.sql import text
import users
import datetime

def add_order(list):
    user_id = users.user_id()
    if user_id == "0":
        username = "anonymous"
    else:
        username = users.username()

    summa = 0
    i = 1

    for item in list:
        summa += int(item)*15
        if int(item) > 0:
            for j in range(int(item)):
                if i == 1:
                    pizza = "Marinara"
                elif i == 2:
                    pizza = "Margherita"
                elif i == 3:
                    pizza = "Pepperoni"
                elif i == 4:
                    pizza = "Salami"
                elif i == 5:
                    pizza = "Hawaii"
                elif i == 6:
                    pizza = "Quattro Formaggi"
                sql = text("INSERT INTO pizza_orders (username, pizza) VALUES (:username, :pizza)")
                db.session.execute(sql, {"username":username, "pizza":pizza})
                db.session.commit()
        i += 1

    sql = text("INSERT INTO orders (username, amount, ordered) VALUES (:username, :amount, NOW())")
    db.session.execute(sql, {"username":username, "amount":summa, "ordered":datetime.datetime.now()})
    db.session.commit()
    return True

def user_total_spending(username):
    sql = text("SELECT SUM(amount) FROM orders WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    return result.fetchone()

def all_user_orders(username):
    sql = text("SELECT amount, ordered FROM orders WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    return result.fetchall()

def get_favorite_pizza(username):
    sql = text("SELECT pizza FROM pizza_orders WHERE username=:username GROUP BY pizza ORDER BY COUNT(pizza) DESC LIMIT 1")
    result = db.session.execute(sql, {"username": username})
    return result.fetchone()
