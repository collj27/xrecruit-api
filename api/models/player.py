import os
from sqlalchemy import Enum
from sqlalchemy.ext.hybrid import hybrid_property
from api import db
from utils.position_enum import PositionEnum
from utils.s3_utils import create_presigned_url


class Player(db.Model):
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
    video_url = db.Column(db.String(200), unique=False, nullable=True) #TODO: should this be stored on S3, like the images?

    #player_stats = db.relationship('PlayerStats', lazy=True)

    @hybrid_property
    def image_url(self):
        return create_presigned_url(self.player_id, os.environ['PLAYER_IMG_BUCKET'], os.environ['PLAYER_IMG_PREFIX'])

    def __repr__(self):
        return f"<Player {self.player_id} >"
