# 받은 LMS ID PW 값으로 세션을 유지한 채 LMS에 정보를 가져옵니다.
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_subject_information(session):


    return_subject_list = []

    subject_craw_url = "https://lms.pknu.ac.kr/ilos/main/main_form.acl" # 학수번호와 과목 명을 크롤링함
    request = session.post(subject_craw_url, verify=False)
    soup = BeautifulSoup(request.text, "html.parser") #main에 요청보내서 학수번호 알아내기
    temp_subject_list = soup.findAll("em", {"sub", "sub_open"})

    for index in range(len(temp_subject_list)):
        return_subject_list.append( [ "".join(temp_subject_list[index].text.replace(" ","").split()), temp_subject_list[index]['kj'] ] )

    return return_subject_list



def get_subject_details_information(subject_list, session):


    craw_url = "https://lms.pknu.ac.kr/ilos/st/course/eclass_room2.acl"
    sub_main = "https://lms.pknu.ac.kr/ilos/st/course/submain_form.acl"

    for index in range(len(subject_list)):
        data = {
        'KJKEY': subject_list[index][1], # n번째 과목의 학수번호
        'returnData': 'json',
        'returnURI': '',
        'encoding': 'utf-8'
        }

        request = session.post(craw_url, data = data, verify = False) # 해당 과목에 대한 session을 얻는다.
        soup = BeautifulSoup(request.text, "html.parser")

        res = session.get(sub_main, verify = False )

        soup = BeautifulSoup(res.text, "html.parser")
        temp_right = soup.find("div", {"class","submain-rightarea"}) # 오른쪽 배너를 부르고
        temp_detail_sub_info = temp_right.findAll("a", {"class", "site-link"}) # 부른 것에서 추출

        # 강의랑 과제만뽑아야함
        print("===" * 35 )
        print("과목명 : " + subject_list[index][0] + "\n",)
        for i in range(len(temp_detail_sub_info)):
            print(temp_detail_sub_info[i].text.strip(), end = " : ")
            print(temp_detail_sub_info[i]['href'])
        print( "\n" * 2)

# a = get_session("201712672", "password")
# subject_list = get_subject_information()
# get_subject_details_information(subject_list)