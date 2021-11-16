"""
test_api Test Case
"""
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
