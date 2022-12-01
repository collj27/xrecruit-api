import json
from flask import Blueprint
from api.db_models.school import School
from api import db
from api.schemas.SchoolSchema import SchoolSchema

# create blueprint
schools_controller_bp = Blueprint('schools_controller', __name__)
school_schema = SchoolSchema()

# fetch all players
@schools_controller_bp.route('/schools', methods=['GET'])
def get_schools():
    result_list = db.session.execute(db.select(School)).scalars().all()
    school_list = [result.to_dict() for result in result_list]

    return school_list


# fetch players by id
@schools_controller_bp.route('/schools/<school_id>', methods=['GET'])
def get_school_by_id(school_id):
    school = db.get_or_404(School, school_id)
    return school_schema.dumps(school)



