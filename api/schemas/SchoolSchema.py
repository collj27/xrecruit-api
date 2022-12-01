from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from api.db_models.school import School


class SchoolSchema(SQLAlchemySchema):
    class Meta:
        model = School

    school_id = auto_field()
    name = auto_field()