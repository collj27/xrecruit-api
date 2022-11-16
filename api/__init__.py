import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# TODO: add flask migration
def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # register blueprints
    from api.controllers.players_controller import players_controller_bp
    app.register_blueprint(players_controller_bp)

    # import models, init db, and create tables
    # TODO: figure out better way to handle model imports
    from api.models import player, player_stats
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
