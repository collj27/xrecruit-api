from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

from api import db


class PlayerInfo(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    position_id = db.Column(db.Integer, unique=False, nullable=False)
    first_name = db.Column(db.String(30), unique=False, nullable=False)
    last_name = db.Column(db.String(30), unique=False, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.String(5), unique=False, nullable=False)
    weight = db.Column(db.Integer, unique=False, nullable=False)
    high_school = db.Column(db.String(30), unique=False, nullable=False)
    birth_date = db.Column(db.Date, unique=False, nullable=False)


def __repr__(self):
    return f"<PlayerInfo {self.id} >"
