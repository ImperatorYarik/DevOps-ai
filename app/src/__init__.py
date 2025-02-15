from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    from .controllers.home_controller import home_bp
    from .controllers.docker_controller import docker_bp
    from .controllers.setup_controller import setup_bp
    from .controllers.settings_controller import settings_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(docker_bp)
    app.register_blueprint(setup_bp)
    app.register_blueprint(settings_bp)

    return app