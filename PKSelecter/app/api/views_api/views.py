"""
static API
"""

from flask import Blueprint, render_template
from api.views_api import views_bp


"""
기본 view를 return
"""
@views_bp.route('/')
def index():
    return render_template("index.html")



