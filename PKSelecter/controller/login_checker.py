# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

# my_server_login_check
# def login_check(pks_user_id, pks_user_pw):
#     if pks_user_id.isdigit() != True and len(pks_user_id) != 9:
#         return False
#     elif len(pks_user_pw) != 6 and not (10 <= len(pks_user_pw) <= 16):
#         return False
#     else:
#         return True
#  => 통합.


# lms_login_check
def login_check_and_get_session(lms_id, lms_pw):
    # 따로 뺄까 했지만 통합.
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

        if "로그인 정보가 일치하지 않습니다." in confirm_login.text:
            session.close()  # 세션 닫기
            return False, "no session"
        else:
            return True, session
