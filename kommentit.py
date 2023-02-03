from sqlalchemy.sql import text
from db import db

def get_list():
    sql = text("SELECT comment, username, posted FROM comments")
    result = db.execute(sql)
    return result.fetchall()

def add_comment(username, comment):
    sql = text("INSERT INTO comments (comment, username, posted) VALUES (:comment, :username, NOW())")
    db.session.execute(sql, {"comment":comment, "username":username})
    db.session.commit()
    return True