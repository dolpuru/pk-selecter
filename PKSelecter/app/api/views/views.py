"""
static API
"""

from flask import Blueprint, render_template
from app.views import views_bp
from app.api import login_api

"""
기본 view를 return
"""
@views_bp.route('/')
def index():
    return render_template("index.html")



