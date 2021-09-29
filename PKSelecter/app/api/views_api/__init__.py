"""
기본 view를 return
"""
from flask import Blueprint, render_template
from .views import main_page


views_bp = Blueprint('views_bp', __name__)
main_page(views_bp, render_template)

