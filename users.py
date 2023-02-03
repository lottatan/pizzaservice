from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
from db import db
from sqlalchemy.sql import text


def create(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)
    
def login(username, password):
    sql = text("SELECT password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["username"] = user.username
            return True
        else:
            return False

def logout():
    try:
        del session["username"]
    except:
        return

def username():
    return session("username", 0)