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

def get_fake():
    fake = Faker('ko_KR')
    fake.add_provider(internet)
    return fake


def fake_request_data(fake_cnt):
    fake = get_fake()

    temp_uri = fake.uri()
    path = ""
    true_path = "/main"
    true_method = "POST"
    true_status = "200"
    special_chr = '[-=+,#/\?:^$.@*"※~&%ㆍ!‘|\(\)\[\]\<\>`\']'

    for i in range(len(temp_uri)-1, -1, -1):
        try:
            path += temp_uri[i] if temp_uri[i] !="/" else 1
        except:
            path = path[::-1]
            break
    
    request_data_result = [{
        'uri': "http://localhost:" + str(80) + true_path,
        'method': true_method,
        'status_code' : true_status,
    
    'form_data_result' :  {
                    "lms_id" : fake.numerify(text="#########"), # 9글자 숫자
                    "lms_pw" : fake.numerify(text="#") + fake.lexify(text= "????" + "?" *
                        ( fake.random_int(min=5, max=11) * fake.random_int(min=0, max=1) ), 
                        letters= (string.ascii_letters + string.digits + special_chr)) + 
                        fake.lexify(text="?", letters = special_chr)
        }, #id는 9글자, 비밀번호는 6자리 숫자(asd) 숫자 특수문자 포함 10자리 이상혹은 최대 16자리 , 첫 데이터는 통과하는 데이터 넣을거라, 항상 숫자 1 특수문자 1 을 포함하도록 하였음.
    'status_code' : "200"
    }
    ]


    request_data_result += (
        {
                'uri': "http://localhost:" + str(fake.random_int(min=0, max=65535)) + "/" + path,
                'method': fake.random_element(elements=('GET', 'POST', 'PUT')),
                
                'form_data_result' :  {
                    "lms_id" : fake.lexify(text= "?"* fake.random_int(min=0, max=18), letters = string.digits + string.ascii_letters ), 
                    "lms_pw" : fake.lexify(text= "?" * fake.random_int(min=0, max=16), letters= (string.ascii_letters + string.digits + special_chr))
        }, #id는 9글자, 비밀번호는 6자리 숫자(asd) 숫자 특수문자 포함 10자리 이상혹은 최대 16자리
        'status_code' : fake.random_element(elements = (200, 400, 404))
        
            } for _ in range(fake_cnt)
    )

    return request_data_result

#form_data_result는 서버 -> lms에도 이용하니까 따로 빼둬야하지 않을까 ? 아니면 요청 하나하나에 힘을 실어야하기에 ㅇㅇ
