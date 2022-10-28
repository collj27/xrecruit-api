from flask import make_response, Blueprint

# create blueprint
players_controller_bp = Blueprint('players_controller', __name__)


@players_controller_bp.route('/', methods=['GET'])
def get_players():
    return make_response(
        'Test worked!',
        200
    )


@players_controller_bp.route('/players_by_id', methods=['GET'])
def get_players_by_id():

    return {
        "Position": "QB",
        "FirstName": "Archie",
        "LastName": "Manning Jr.",
        "Description": "Arch Manning, the No. 1-ranked player in 247Sports' Class of 2023, made huge waves"
                       "Thursday by ending his whirlwind recruitment and announcing his"
                       "commitment to Texas over Alabama and Georgia. Manning, the nephew of legendary"
                       "quarterbacks Peyton and Eli Manning and grandson to College Football Hall of Famer Archie"
                       "Manning, has been the most sought-after recruiting prospect since the days of Trevor Lawrence"
                       "and Justin Fields."
    }
