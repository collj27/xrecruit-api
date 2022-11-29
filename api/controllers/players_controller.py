import os

from flask import Blueprint
from api.models.player import db, Player
from utils.s3_utils import create_presigned_url

# create blueprint
players_controller_bp = Blueprint('players_controller', __name__)


# fetch all players
@players_controller_bp.route('/players', methods=['GET'])
def get_players():
    result_list = db.session.execute(db.select(Player)).scalars().all()
    player_list = [result.to_dict() for result in result_list]

    return player_list


# fetch players by id
@players_controller_bp.route('/players/<player_id>', methods=['GET'])
def get_player_by_id(player_id):
    player_info = db.get_or_404(Player, player_id).to_dict()
    url = create_presigned_url(player_id, os.environ['PLAYER_IMG_BUCKET'], os.environ['PLAYER_IMG_PREFIX'])
    player_info['player_img_url'] = url

    return player_info
