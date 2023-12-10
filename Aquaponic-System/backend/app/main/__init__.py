from flask import Blueprint

print("WASASASAS")
main_bp = Blueprint('main', __name__)

from . import routes
