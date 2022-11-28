from sqlalchemy import Enum
from sqlalchemy_serializer import SerializerMixin
from api import db
from utils.position_enum import PositionEnum


class School(db.Model, SerializerMixin):
    __tablename__ = "schools"
    school_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)


def __repr__(self):
    return f"<School {self.school_id}>"
