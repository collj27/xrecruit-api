from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from api import db


class PositionLookup(db.Model, SerializerMixin):
    position_id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(5), unique=False, nullable=False)


def __repr__(self):
    return f"<Position {self.position} >"
