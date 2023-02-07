from sqlalchemy.sql import text
from db import db
import datetime

def get_list():
    sql = text("""SELECT comment, username, posted FROM comments""")
    result = db.session.execute(sql)
    return result.fetchall()

def add_comment(username, comment):
    sql = text("""INSERT INTO comments (comment, username, posted) VALUES (:comment, :username, NOW())""")
    db.session.execute(sql, {"comment":comment, "username":username, "posted":datetime.datetime.now()})
    db.session.commit()
    return True