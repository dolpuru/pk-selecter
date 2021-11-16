"""
test_login_checker Test Case
"""
# api에 테스트 해보기 위한 데이터 생성 부분입니다.
# 어떤 필요한 데이터들을 생성해서 test를 해볼 것인가?를 주된 관점으로 작성해보았습니다.
# 서버에 대한 API 요청을 테스트 해볼 것이기에, 이에 필요한 요소들을 정리해보겠습니다.

import sys, os
import json
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) #app을 import 하기 위함


from app import create_app
from config import config_dict

import unittest
from make_fake_data import fake_request_data


class MyTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_dict['testing'])
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

  
    def test_login_fail(self):
        print("\n>>>>가짜 데이터를 생성하고, login_api를 검증해봅니다<<<< \n")
        print(">>>생성할 가짜 데이터의 갯수를 입력해주세요 : ")
        cnt = int(input())
        print("\n")
        fake_data = fake_request_data(cnt)

        for index in range(cnt):
            resp = self.client.post(
                fake_data[index]['path'],
                data = json.dumps(dict(
                fake_data[index]['form_data_result']
                )), 
                content_type = 'application/json', 
                follow_redirects = True)
            
            format_resp = json.loads(resp.data.decode('utf-8'))
            print("테스트 데이터 : ", fake_data[index]['form_data_result'])
            print("응답 데이터 : ", format_resp)


            self.assertEqual(format_resp['status'],  fake_data[index]['status_code'])
            print(">>>검증 완료<<< \n")
    
    # def test_login_sucess(self):
