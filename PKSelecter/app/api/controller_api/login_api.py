# 사용자가 main_page.py에서 로그인하면, login_Check랑 이어져서 , login_Check에서 주는 값을 그대로 return해야함
from flask import request, render_template
from controller import login_checker, selecter

"""
login_checker에 해당 값을 보냄
"""


def login_router(login_bp):
    @login_bp.route("/login", methods=["POST"])
    def login_api():

        pks_user_id = request.form["pk_user_id"]
        pks_user_pw = request.form["pk_user_pw"]
        return_value, return_session = login_checker.login_check_and_get_session(
            pks_user_id, pks_user_pw
        )
        return render_template("index_2.html", id=pks_user_id, pw=pks_user_pw)

        if return_value == False:
            return {"error_msg": "올바른 ID혹은 PW가 아닙니다."}

        elif return_value == True:
            unoragnized_data = selecter.get_subject_information(return_session)
            json_data = json_handler.oragnized(unoragnized_data)

        return json_data
