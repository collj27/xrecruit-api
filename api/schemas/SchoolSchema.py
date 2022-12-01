from marshmallow_sqlalchemy import SQLAlchemySchema

from api.db_models.school import School


class SchoolSchema(SQLAlchemySchema):
    class Meta:
        model = School
        fields = ["school_id", "name", "image_url", "news_articles"]
