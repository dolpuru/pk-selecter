"""
기본 view를 return
"""
from flask import Blueprint
from .views import views_router


views_bp = Blueprint(
    "views_bp", 
    __name__, 
)
views_router(views_bp)
