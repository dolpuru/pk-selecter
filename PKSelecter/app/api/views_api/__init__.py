"""
기본 view를 return
"""
from flask import Blueprint
from flask import app, render_template

views_bp = Blueprint("views_bp", __name__)


from . import views
