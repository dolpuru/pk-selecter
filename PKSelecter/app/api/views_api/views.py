from flask import render_template, app
from app.api.views_api import views_bp

def main_page(bp, render_template):
    @bp.route('/main')
    def index():
        return render_template("index.html")
# @views_deco
# @app.route('/main')
# def index():
#     return render_template("index.html")