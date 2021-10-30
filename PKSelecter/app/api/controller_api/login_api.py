# 사용자가 main_page.py에서 로그인하면, login_Check랑 이어져서 , login_Check에서 주는 값을 그대로 return해야함
from flask import request, render_template
from controller import login_checker, selecter

"""
login_checker에 해당 값을 보냄
"""


def login_router(login_bp):
    @login_bp.route("/login", methods=["POST"])
    def login_api():
        json_data = request.get_json()

        pk_user_id = json_data["pk_user_id"]
        pk_user_pw = json_data["pk_user_pw"]
        login_check_value = login_checker.login_check_and_get_session(
            pk_user_id, pk_user_pw
        )

        if login_check_value == False:
            return {"error_msg": "올바른 ID혹은 PW가 아닙니다."}

        elif login_check_value == True:
            unoragnized_data = selecter.get_subject_information(pk_user_id, pk_user_pw)

        return unoragnized_data
