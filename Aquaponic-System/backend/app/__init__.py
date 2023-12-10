from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """
    Create and configure the Flask application.

    

    Overview:
    - Initializes a Flask app.
    - Configures the app using the Config class.
    - Initializes the SQLAlchemy database.
    - Sets up database migrations using Flask-Migrate.
    - Creates database tables.
    - Registers blueprints for modularization.

    Usage:
    - Use this function to create the Flask app instance for your project.

    Dependencies:
    - Flask
    - Flask-SQLAlchemy
    - Flask-Migrate
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        try:
            # Create the database tables
            db.create_all()
        except Exception as e:
            print(f"Error creating database tables: {str(e)}")

    # Register blueprints
    from app.main import main_bp
    app.register_blueprint(main_bp)

    from app.equaponic import equaponic_blueprint
    app.register_blueprint(equaponic_blueprint)

    from app.plants import plants_blueprint
    app.register_blueprint(plants_blueprint)

    from app.arduino_api import arduino_api_blueprint
    app.register_blueprint(arduino_api_blueprint)

    from app.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
