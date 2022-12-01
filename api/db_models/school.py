import os

import requests
from marshmallow import Schema
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
        return self.name
    #def __init__(self):
   #     self.image_url = None
    #    self.video_url = None
   #     self.news_articles = None

    def __repr__(self):
        return f"<School {self.school_id}>"


#@event.listens_for(School, 'load')
def receive_load(target, context):
    # fetch imagee url after load
    target.image_url = create_presigned_url(target.school_id, os.environ['SCHOOL_IMG_BUCKET'],
                                            os.environ['SCHOOL_IMG_PREFIX'])

    # search for recent news after load
    search_query = target.name + " football news"
    request_string = "https://www.googleapis.com/customsearch/v1?" \
                     "key={api_key}" \
                     "&cx={search_engine_id}" \
                     "&q={query}" \
                     "&num=5".format(api_key=os.environ['GOOGLE_API_KEY'],
                                     search_engine_id=os.environ['SEARCH_ENGINE_ID'], query=search_query)
    target.news_articles = requests.get(request_string).json()

    target.video_url = "test"
