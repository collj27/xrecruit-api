import os

import requests
from sqlalchemy import Enum, event
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from api import db
from utils.position_enum import PositionEnum
from utils.s3_utils import create_presigned_url


class School(db.Model):
    __tablename__ = "schools"
    school_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    @hybrid_property
    def image_url(self):
        return create_presigned_url(self.school_id, os.environ['SCHOOL_IMG_BUCKET'],
                                            os.environ['SCHOOL_IMG_PREFIX'])

    @hybrid_property
    def news_articles(self):
        # TODO: move this to controller
        # search for recent news after load
        search_query = self.name + " football news"
        request_string = "https://www.googleapis.com/customsearch/v1?" \
                         "key={api_key}" \
                         "&cx={search_engine_id}" \
                         "&q={query}" \
                         "&num=5".format(api_key=os.environ['GOOGLE_API_KEY'],
                                         search_engine_id=os.environ['SEARCH_ENGINE_ID'], query=search_query)
        return requests.get(request_string).json()

    def __repr__(self):
        return f"<School {self.school_id}>"



