import json
import os

import requests
from flask import Blueprint
from api.db_models.school import School
from api import db
from api.schemas.SchoolSchema import SchoolSchema

# create blueprint
schools_controller_bp = Blueprint('schools_controller', __name__)
school_schema = SchoolSchema()


def _fetch_news_articles(school):
    search_query = school.name + " football news"
    request_string = "https://www.googleapis.com/customsearch/v1?" \
                     "key={api_key}" \
                     "&cx={search_engine_id}" \
                     "&q={query}" \
                     "&num=5".format(api_key=os.environ['GOOGLE_API_KEY'],
                                     search_engine_id=os.environ['SEARCH_ENGINE_ID'], query=search_query)
    return requests.get(request_string).json()


# fetch all players
# @schools_controller_bp.route('/schools', methods=['GET'])
# def get_schools():
#    result_list = db.session.execute(db.select(School)).scalars().all()
#    school_list = [result.to_dict() for result in result_list]

#    return school_list


# fetch players by id
@schools_controller_bp.route('/schools/<school_id>', methods=['GET'])
def get_school_by_id(school_id):
    # fetch school and associated news articles
    school = db.get_or_404(School, school_id)
    news_articles = _fetch_news_articles(school)

    # convert school object to dict and add news articles
    school_dict = school_schema.dump(school)
    school_dict['news_articles'] = news_articles["items"]

    # serialize and return
    return json.dumps(school_dict)
