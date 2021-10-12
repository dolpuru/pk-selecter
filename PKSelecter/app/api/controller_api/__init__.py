"""
Sample API Module Package
"""
from flask import Blueprint, render_template, request


controller_bp = Blueprint("controller_bp", __name__)


def views_deco(func):

    return func


@controller_bp.route("/", methods=["POST"])
@views_deco
def index():
    pks_user_id = request.form["pk_user_id"]
    pks_user_pw = request.form["pk_user_pw"]
    # return_value, return_session = login_checker.login_check_and_get_session(
    #     pks_user_id, pks_user_pw
    # )
    return render_template("index_2.html", id=pks_user_id, pw=pks_user_pw)
