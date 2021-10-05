"""
기본 view를 return
"""
from flask import Blueprint
from flask import app
def views_deco(func):
    Blueprint('views_bp', __name__)
    return func

