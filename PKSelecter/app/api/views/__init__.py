from flask import Blueprint

views_bp = Blueprint('views_bp', __name__)

from . import views_bp