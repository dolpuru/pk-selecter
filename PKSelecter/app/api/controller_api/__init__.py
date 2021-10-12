"""
로그인 확인 및 LMS데이터를 return
"""
from flask import Blueprint
from .login_api import login_router


controller_bp = Blueprint("controller_bp", __name__)
login_router(controller_bp)
