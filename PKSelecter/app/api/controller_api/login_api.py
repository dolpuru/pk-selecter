# 사용자가 main_page.py에서 로그인하면, login_Check랑 이어져서 , login_Check에서 주는 값을 그대로 return해야함
import flask
from controller import login_checker, selecter, json_handler
from controller_api import controller_bp
from flask import request
"""
login_checker에 해당 값을 보냄
"""
@controller_bp.route('/login', methods=["POST"])
def index():
    pks_user_id = request.form['pks_user_id']
    pks_user_pw = request.form['pks_user_pw']
    return_value, return_session = login_checker.login_check_and_get_session(pks_user_id, pks_user_pw) 
    if return_value == False:
        return {"error_msg" : "올바른 ID혹은 PW가 아닙니다."}

    elif return_value == True:

        login_checker.login_check(pks_user_id, pks_user_pw) # T/F?