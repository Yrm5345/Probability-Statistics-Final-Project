from flask import Blueprint

equaponic_blueprint = Blueprint('equaponic', __name__)

from . import routes
