"""
기본 view를 return
"""
from flask import Blueprint
from flask import app, render_template

views_bp = Blueprint('views_bp', __name__)

def views_deco(func):
        
    return func

@views_bp.route("/main")
@views_deco
def index():
    return render_template("index.html")


# from . import views