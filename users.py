from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
from db import db
from sqlalchemy.sql import text
import os


def create(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("""INSERT INTO users (username, password) VALUES (:username, :password)""")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    
    return login(username, password)

    
def login(username, password):
    sql = text("""""SELECT id, password FROM users WHERE username=:username""")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user[2], password):
            session["user_id"] = user[0]
            session["username"] = username
            session["csrf_token"] = os.urandom(16).hex()
            return True


def logout():
    try:
        del session["user_id"]
        del session["username"]
        del session["csrf_token"]
    except:
        return

def user_id():
    return session("user_id", 0)

def username():
    return session("username", 0)