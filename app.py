import os
from flask import Flask
from models.player_info import db # TODO: move db elsewhere


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # init db and create tables
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # register blueprints
    from controllers.players_controller import players_controller_bp
    app.register_blueprint(players_controller_bp)

    return app


if __name__ == '__main__':
    create_app()
