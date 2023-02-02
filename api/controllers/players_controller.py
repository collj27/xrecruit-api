import os

from flask import Blueprint
from sqlalchemy import select

from api.models.player import db, Player
from api.models.player_stats import PlayerStats
from api.schemas.PlayerSchema import PlayerSchema
from api.schemas.PlayerStatsSchema import PlayerStatsSchema
from utils.s3_utils import create_presigned_url

# create blueprint
players_controller_bp = Blueprint('players_controller', __name__)
player_schema = PlayerSchema()
player_stats_schema = PlayerStatsSchema()


# fetch all players
@players_controller_bp.route('/GetPlayers', methods=['GET'])
def get_players():
    stmt = select(Player)
    players = db.session.scalars(stmt).all()

    return player_schema.dumps(players, many=True)


# fetch players by id
@players_controller_bp.route('/GetPlayerById/<int:player_id>', methods=['GET'])
def get_player_by_id(player_id):
    player_info = db.get_or_404(Player, player_id)

    return player_schema.dumps(player_info)


@players_controller_bp.route('/GetPlayerStats/<int:player_id>', methods=['GET'])
def get_player_stats(player_id):
    stmt = select(PlayerStats).where(PlayerStats.player_id == player_id)
    stats = db.session.scalars(stmt).all()

    return player_stats_schema.dumps(stats, many=True)
