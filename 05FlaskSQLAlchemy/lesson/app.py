from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from typing import List

app: Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']: str = 'sqlite:///example.db'
db: SQLAlchemy = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

with app.app_context():
    db.create_all()

    # new_user: User = User(username='t', email='t@example.com')
    # db.session.add(new_user)
    # db.session.commit()

    # Fetching all users
    all_users: List[User] = User.query.all()

    # Fetching a user by id
    user_obj: User = db.session.get(User, 1)

    if user_obj:
        print(user_obj.email)

    user_obj: User = db.session.get(User, 1)

    if user_obj:
        user_obj.email = 'new5_email@example.com'
        db.session.commit()
        print(user_obj.email)  # new5_email@example.com

    # Fetching a user by id
    user_obj: User = db.session.get(User, 1)

    if user_obj:
        db.session.delete(user_obj)
        db.session.commit()