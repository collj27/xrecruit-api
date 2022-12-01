from sqlalchemy_serializer import SerializerMixin
from api import db


class PlayerStats(SerializerMixin):
    stats_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.player_id"), nullable=False)
    season = db.Column(db.Integer, unique=False, nullable=False)
    passing_tds = db.Column(db.Integer, unique=False, nullable=True)
    passing_yds = db.Column(db.Integer, unique=False, nullable=True)
    rushing_tds = db.Column(db.Integer, unique=False, nullable=True)
    rushing_yds = db.Column(db.Integer, unique=False, nullable=True)
    interceptions = db.Column(db.Integer, unique=False, nullable=True)
    fumbles = db.Column(db.Integer, unique=False, nullable=True)


def __repr__(self):
    return f"<QBStats {self.stats_id} >"
