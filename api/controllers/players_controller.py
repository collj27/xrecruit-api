import os

from flask import Blueprint
from api.models.player import db, Player
from api.schemas.PlayerSchema import PlayerSchema
from api.schemas.PlayerStatsSchema import PlayerStatsSchema
from utils.s3_utils import create_presigned_url

# create blueprint
players_controller_bp = Blueprint('players_controller', __name__)
player_schema = PlayerSchema()
player_stats_schema = PlayerStatsSchema()


# fetch all players
@players_controller_bp.route('/players', methods=['GET'])
def get_players():
    result_list = db.session.query(Player)
    return player_schema.dumps(result_list, many=True)


# fetch players by id
@players_controller_bp.route('/players/<player_id>', methods=['GET'])
def get_player_by_id(player_id):
    player_info = db.get_or_404(Player, player_id)

    return player_schema.dumps(player_info)

