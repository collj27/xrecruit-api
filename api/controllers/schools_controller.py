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
    search_parameter = school_info['name'] + " AND College AND Football"

    # TODO: adjust these parameters
    # get news articles by school name
    request_string = "https://newsapi.org/v2/everything?" \
                     "q={keywords}" \
                     "&pageSize=5" \
                     "&searchIn=title,description" \
                     "&apiKey={api_key}".format(keywords=search_parameter, api_key=os.environ['NEWS_API_KEY'])
    print(request_string)
    news = requests.get(request_string).json()

    # add news to school object
    school_info['news'] = news

    # add logo url
    url = create_presigned_url(school_id, os.environ['SCHOOL_IMG_BUCKET'], os.environ['SCHOOL_IMG_PREFIX'])
    school_info['school_img_url'] = url

    return school_info
