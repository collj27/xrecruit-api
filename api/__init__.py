import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, upgrade, migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate_config = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # register blueprints
    from api.controllers.players_controller import players_controller_bp
    app.register_blueprint(players_controller_bp)

    from api.controllers.schools_controller import schools_controller_bp
    app.register_blueprint(schools_controller_bp)

    from api.controllers.payments_controller import payments_controller_bp
    app.register_blueprint(payments_controller_bp)

    CORS(app, CORS_ORIGINS=os.environ['CORS_ORIGINS'])

    # import models, init db, and create tables
    # TODO: figure out better way to handle model imports
    from api.models import player, player_stats, school, payment
    db.init_app(app)
    migrate_config.init_app(app, db)

    with app.app_context():
        db.create_all()
        migrate(directory='migrations')
        upgrade(directory='migrations')

    return app
