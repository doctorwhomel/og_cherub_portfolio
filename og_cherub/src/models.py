from cgitb import text
from typing import Text
from flask_sqlalchemy import SQLAlchemy
import datetime

import pytest

db = SQLAlchemy()

# accounts_table = db.Table(
#     'user_accounts',

#     db.Column(
#         'id', db.Integer,
#         primary_key=True
#     ),

#     db.Column(
#         'user_name', db.Text,
#         nullable=False

#     ),

#     db.Column(
#         'password', db.Text,
#         nullable=False
#     )
# )

class User (db.Model):
    __tablename__ = 'user_accounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password

    def serialize(self):
        return {
            'user_name': self.user_name,
            'password': self.password,
        }


class Profile (db.Model):
    __tablename__ = 'user_profiles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seeking = db.Column(db.String(128))
    min_age = db.Column(db.Integer)
    max_age = db.Column(db.Integer)
    name = db.Column(db.String(128))
    user_location = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(128), nullable=False)
    user_account_id = db.Column(db.Integer, nullable=False)

    def __init__(self, id: int, name: str, gender: str, age: int, user_location: str, seeking: str, min_age: int, max_age: int, user_account_id: int):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age
        self.user_location = user_location
        self.seeking = seeking
        self.min_age = min_age
        self.max_age = max_age
        self.user_account_id = user_account_id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age,
            'location': self.user_location,
            'seeking': self.seeking,
            'min age': self.min_age,
            'max age': self.max_age,
            'account ID': self.user_account_id

        }


class Pick (db.Model):
    __tablename__ = 'top_picks'
    user_id = db.Column(db.Integer, primary_key=True)
    pick_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, user_id: int, pick_id: int):
        self.user_id = user_id
        self.pick_id = pick_id

    def serialize(self):
        return {
            'user': self.user_id,
            'pick': self.pick_id,
        }
