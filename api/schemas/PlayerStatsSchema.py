from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.db_models.player_stats import PlayerStats


class PlayerStatsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PlayerStats
        include_fk = True
