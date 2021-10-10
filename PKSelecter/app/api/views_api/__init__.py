"""
기본 view를 return
"""
from flask import Blueprint
from flask import app

bp = Blueprint('views_bp', __name__)

def views_deco(func):

    def inner(*args, **kwargs):
        @bp.route(location)
        func(*args, **kwargs)
        
    return inner


# from . import views