from flask import render_template, app
from app.api.views_api import views_bp


def views_deco(func):

    return func


@views_bp.route("/")
@views_deco
def index():
    return render_template("index.html")
