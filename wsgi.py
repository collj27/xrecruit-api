from flask import Flask
from flask_cors import CORS

from utils.cors_config import CorsConfig


def create_app():
    app = Flask(__name__)
    cors_config = CorsConfig()

    CORS(app,
         origins=[cors_config.CORS_ALLOW_ORIGIN],
         supports_credentials=cors_config.CORS_SUPPORTS_CREDENTIALS)

    # Set the configurations
    app.config.from_object(cors_config)

    # register blueprints
    from controllers.players_controller import players_controller_bp
    app.register_blueprint(players_controller_bp)

    return app
