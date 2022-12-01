from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy import event

from api.db_models.player import Player
from api.db_models.player_stats import PlayerStats
from utils.position_enum import PositionEnum


#@event.listens_for(PlayerStats, 'init')
class PlayerSchema(SQLAlchemySchema):
    class Meta:
        model = Player
        include_relationships = True
        fields.Enum(PositionEnum)

    player_id = auto_field()
    #position = auto_field()
    first_name = auto_field()
    last_name = auto_field()
    description = auto_field()
    height = auto_field()
    weight = auto_field()
    high_school = auto_field()
    birth_date = auto_field()
    player_stats = auto_field()

