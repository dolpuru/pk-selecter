# 사용자가 main_page.py에서 로그인하면, login_Check랑 이어져서 , login_Check에서 주는 값을 그대로 return해야함
from controller import login_checker, selecter, json_handler
from controller_api import controller_bp
"""
login_api에 해당 값을 보냄
"""
@controller_bp.route('/login_checker')
def index():
    pass
    # login_api
    #requests.form['lms_id'], 'lms_pw'
    # return render_template("index.html")