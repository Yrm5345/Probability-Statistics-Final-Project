from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS
import flask_login 

db = SQLAlchemy()
migrate = Migrate()

def create_app():
   
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager = flask_login.LoginManager(app)
    login_manager.login_view = 'auth.login'
    

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

    with app.app_context():
        try:
            # Create the database tables
            db.create_all()
            print("All tables created")
        except Exception as e:
            print(f"Error creating database tables: {str(e)}")

    return app
