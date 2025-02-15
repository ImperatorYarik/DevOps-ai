from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__,
                template_folder='templates',  # Add template folder configuration
                static_folder='static')
    app.config.from_object(Config)

    # Register blueprints
    from src.controllers.home_controller import home_bp
    from src.controllers.docker_controller import docker_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(docker_bp)

    return app