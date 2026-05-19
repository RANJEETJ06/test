from app.database import db

def get_users():
    return db.fetch_all()

def add_user(user, users=[]):
    users.append(user)
    return users