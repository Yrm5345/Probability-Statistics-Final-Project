from flask import Blueprint

arduino_api_blueprint = Blueprint('arduino_api', __name__)

from . import routes
