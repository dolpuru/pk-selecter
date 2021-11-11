from flask import request
from controller import login_check, selecter

"""
controller/login_checker.py에 해당 값을 보냄
"""
def login_router(login_bp):
    @login_bp.route("/login", methods=["POST"])
    def login_api():
        json_data = request.get_json()

        pk_user_id = json_data["pk_user_id"]
        pk_user_pw = json_data["pk_user_pw"]

        login_check_value = login_check.login_check_and_get_session(
            pk_user_id, pk_user_pw
        )

        if login_check_value == False:
            return {"status": 400, "error_msg": "올바른 ID혹은 PW가 아닙니다."}

        elif login_check_value == True:
            unoragnized_data = selecter.get_subject_information(pk_user_id, pk_user_pw)

        return unoragnized_data
