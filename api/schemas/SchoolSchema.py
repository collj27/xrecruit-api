from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from api.db_models.school import School


class SchoolSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = School

    image_url = fields.String()  # explicitly define hybrid property
