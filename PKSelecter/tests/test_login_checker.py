#라우터 포함되어 있음 
"""
test_login_checker Test Case
"""
import unittest
# from app import create_app
# from config import config_dict as config
from faker import Faker
from faker.providers import internet
import string
# api에 테스트 해보기 위한 데이터 생성 부분입니다.
# 어떤 필요한 데이터들을 생성해서 test를 해볼 것인가?를 주된 관점으로 작성해보았습니다.
# 서버에 대한 API 요청을 테스트 해볼 것이기에, 이에 필요한 요소들을 정리해보겠습니다.
'''
클라이언트 => 서버에 대한 요청 자체에 대한 Test입니다. 
서버 => LMS서버에 대한 요청이 아닙니다...?
1. 파라메타 (GET, POST, PUT, DELETE 4개)
2. uri 에서 url을 뺀 부분 ( path 부분 ) # 제 서버로 보내야 의미가 있다고 생각했습니다., path부분의 임의의 문자로 지정하지 않은 이유는 fake에서 제공하는 path를 이용하고 싶어서 입니다.
4. port 번호
3. 2번에서 추출한 값을 http://localhost:포트번호/path 로 지정하고, 이 uri들을 저장
5. 3번에서 저장한 값을 GET, POST, PUT, DELETE에 맞게 요청이 올바른지 에 대한 TDD 진행

ex) http://localhost:80/main 으로 POST요청이 200이면 이건 잘못됐습니다. 로 하고 나머지는  전부 400 Bad Request로 처리가 되는지 확인하는 코드입니다. header, parameter등의 요소는 처리하지 않았습니다.

클라이언트 -> 서버 form data 부분은 따로 빼서 문법체크만 할 것입니다.
'''
'''
input : lms_id, lms_pw
False값을 받아야하는 데이터
if lms_id.isdigit() != True and len(lms_id) != 9:
        return False
    elif len(lms_pw) != 6 and not (10 <= len(lms_pw) <= 16):
        return False
이외에는 통과 할 것
else:
=====>
'''