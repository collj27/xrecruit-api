import os
from sqlalchemy.ext.hybrid import hybrid_property
from api import db
from utils.s3_utils import create_presigned_url


class School(db.Model):
    __tablename__ = "schools"
    school_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    @hybrid_property
    def image_url(self):
        return create_presigned_url(self.school_id, os.environ['SCHOOL_IMG_BUCKET'], os.environ['SCHOOL_IMG_PREFIX'])

    def __repr__(self):
        return f"<School {self.school_id}>"
