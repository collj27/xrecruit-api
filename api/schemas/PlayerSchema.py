from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.models.player import Player
from api.schemas.PlayerStatsSchema import PlayerStatsSchema
from marshmallow_sqlalchemy.fields import Nested
from utils.position_enum import PositionEnum


class PlayerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Player
        include_relationships = True

    player_stats = Nested(PlayerStatsSchema, many=True)
    image_url = fields.String()  # explicitly define hybrid property
    position = fields.Enum(PositionEnum, by_value=False)  # serialize enum by key
