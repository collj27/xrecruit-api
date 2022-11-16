import json

from flask import make_response, Blueprint
from models.player_info import db, PlayerInfo

# create blueprint
players_controller_bp = Blueprint('players_controller', __name__)


@players_controller_bp.route('/test', methods=['GET'])
def get_players_by_id():
    # player_info = db.session.execute(db.select(PlayerInfo).filter_by(id=1)).one()
    player_info = db.get_or_404(PlayerInfo, 1)

    return player_info.to_dict()


@players_controller_bp.route('/players', methods=['GET'])
def get_players():
    result_list = db.session.execute(db.select(PlayerInfo)).scalars().all()
    player_list = [result.to_dict() for result in result_list]

    return player_list
