from flask import Blueprint

plants_blueprint = Blueprint('plants', __name__)

from . import routes
