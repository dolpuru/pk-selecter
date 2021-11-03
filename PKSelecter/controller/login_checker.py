# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

"""
lms_login_check
"""
def login_check_and_get_session(lms_id, lms_pw):

    fail_login_value = "로그인 정보가 일치하지 않습니다."

    if lms_id.isdigit() != True and len(lms_id) != 9:
        return False
    elif len(lms_pw) != 6 and not (10 <= len(lms_pw) <= 16):
        return False
    else:

        session = requests.Session()

        session_url = "https://lms.pknu.ac.kr/ilos/lo/login.acl"  # 세션을 얻을 url

        data = {"usr_id": lms_id, "usr_pwd": lms_pw}  # LMS 아이디  # LMS 비밀번호

        request = session.post(session_url, data=data, verify=False)

        confirm_login = BeautifulSoup(request.text, "html.parser")

        if fail_login_value in str(confirm_login):
            session.close()
            print("세션이 닫혔습니다.")
            return False
        else:
            return True
