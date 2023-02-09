from flask import session, request, abort
from db import db
from sqlalchemy.sql import text
import users
import datetime

def add_order(list):
    username = users.username()
    summa = 0

    for item in list:
        summa += int(item)*15

    sql = text("INSERT INTO orders (username, amount, ordered) VALUES (:username, :amount, NOW())")
    db.session.execute(sql, {"username":username, "amount":summa, "ordered":datetime.datetime.now()})
    db.session.commit()
    return True