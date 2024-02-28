from flask import Blueprint

produto_bp = Blueprint('produto', __name__)

from . import routes
