from app.database import db

def get_users():
    return db.fetch_all()