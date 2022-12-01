from sqlalchemy import Enum
from sqlalchemy_serializer import SerializerMixin
from api import db
from utils.position_enum import PositionEnum


class Player(db.Model, SerializerMixin):
    __tablename__ = "players"
    player_id = db.Column(db.Integer, primary_key=True)
    position = db.Column(Enum(PositionEnum), unique=False, nullable=False)
    first_name = db.Column(db.String(30), unique=False, nullable=False)
    last_name = db.Column(db.String(30), unique=False, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.String(5), unique=False, nullable=False)
    weight = db.Column(db.Integer, unique=False, nullable=False)
    high_school = db.Column(db.String(30), unique=False, nullable=False)
    birth_date = db.Column(db.DateTime, unique=False, nullable=False)
    player_stats = db.relationship('PlayerStats', lazy=True)


def __repr__(self):
    return f"<Player {self.player_id} >"
