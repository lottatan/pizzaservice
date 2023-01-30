from werkzeug.security import check_password_hash, generate_password_hash
import app


def create(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        app.db.session.execute(sql, {"username":username, "password":hash_value})
        app.db.session.commit()
    except:
        return False
    

