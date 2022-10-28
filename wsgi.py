#from flask import Flask
#from app.controllers.players_controller import players_controller_bp

# create application object and register blueprints
#app = Flask(__name__)
#app.register_blueprint(players_controller_bp)

# Run app
#if __name__ == '__main__':
 #   app.run()

from app.main import app

if __name__ == "__main__":
        app.run()
