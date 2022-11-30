import os

from flask import Blueprint
from api.models.player import db, Player
from api.models.school import School
from utils.s3_utils import create_presigned_url
import requests

# create blueprint
schools_controller_bp = Blueprint('schools_controller', __name__)


# fetch all players
@schools_controller_bp.route('/schools', methods=['GET'])
def get_schools():
    result_list = db.session.execute(db.select(School)).scalars().all()
    school_list = [result.to_dict() for result in result_list]

    return school_list


# fetch players by id
@schools_controller_bp.route('/schools/<school_id>', methods=['GET'])
def get_school_by_id(school_id):

    # get school object
    school_info = db.get_or_404(School, school_id).to_dict()
    search_query = school_info['name'] + " football news"

    # TODO: adjust these parameters
    #https://developers.google.com/custom-search/v1/introduction
    # get news articles by school name
    request_string = "https://www.googleapis.com/customsearch/v1?" \
                     "key={api_key}" \
                     "&cx={search_engine_id}" \
                     "&q={query}" \
                     "&num=5".format(api_key=os.environ['GOOGLE_API_KEY'],
                                     search_engine_id=os.environ['SEARCH_ENGINE_ID'], query=search_query)
    news = requests.get(request_string).json()
    school_info['news'] = news['items']

    # add logo url
    url = create_presigned_url(school_id, os.environ['SCHOOL_IMG_BUCKET'], os.environ['SCHOOL_IMG_PREFIX'])
    school_info['school_img_url'] = url

    return school_info
