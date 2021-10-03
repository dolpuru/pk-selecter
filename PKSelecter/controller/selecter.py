# 받은 LMS ID PW 값으로 세션을 유지한 채 LMS에 정보를 가져옵니다.
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def get_subject_information(session):

    return_subject_list = []

    return_str = ""

    subject_craw_url = "https://lms.pknu.ac.kr/ilos/main/main_form.acl" # 학수번호와 과목 명을 크롤링함
    request = session.post(subject_craw_url, verify=False)
    soup = BeautifulSoup(request.text, "html.parser") #main에 요청보내서 학수번호 알아내기
    temp_subject_list = soup.findAll("em", {"sub", "sub_open"})

    for index in range(len(temp_subject_list)):
        return_subject_list.append( [ "".join(temp_subject_list[index].text.replace(" ","").split()), temp_subject_list[index]['kj'] ] )

    subject_list = return_subject_list

    craw_url = "https://lms.pknu.ac.kr/ilos/st/course/eclass_room2.acl"
    sub_main = "https://lms.pknu.ac.kr/ilos/st/course/submain_form.acl"
    assignment_url = "https://lms.pknu.ac.kr"
    online_list = "https://lms.pknu.ac.kr/ilos/st/course/online_list.acl"

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
        return_str += "===" *35 + "\n"
        # print("===" * 35 )
        return_str += "과목명 : " + subject_list[index][0] + "\n"
        # print("과목명 : " + subject_list[index][0] + "\n",)
        temp_list = []
        temp_list2 = []
        # 오른쪽 부분을 이용해서 "과제와 시험기간이 현재 범위 인것만 긁는다." 
        for i in range(len(temp_detail_sub_info)):
            if "[과제]" in temp_detail_sub_info[i].text.strip():
                temp_list.append(assignment_url + temp_detail_sub_info[i]['href'])  
            if "[시험]" in temp_detail_sub_info[i].text.strip():
                print(temp_detail_sub_info[i]['href'])
                temp_list2.append(assignment_url + temp_detail_sub_info[i]['href'])


# 수업 처리 부분
        return_str += "<수업> : \n"
        try:
            data = {
                'ud': "",
                'ky': subject_list[index][1],
                'WEEK_NO': "",
                'encoding': 'utf-8'
            }
            res = session.post(online_list, verify = False)
            
            soup = BeautifulSoup(res.text, "html.parser")
            temp_temp = soup.findAll("div", {"class","lecture-box"})
            for i in range(len(temp_temp)):
                temp_list_find = temp_temp[i].text.split()
                # print(temp_list_find)
                if int(temp_list_find[-4][:-1]) < 100:
                    index_ha = temp_list_find.index("학습인정기간")
                    if "아닙니다." not in temp_list_find[:index_ha]:
                        return_str += str(temp_list_find[:index_ha]) + " " + str(temp_list_find[index_ha + 6: index_ha + 9]) + " " + "까지 수강을 완료하셔야합니다.\n"
                        # print(temp_list_find[:index_ha], temp_list_find[index_ha + 6: index_ha + 9], "까지 수강을 완료하셔야합니다.")
        except:
            # print("들으실 강의가 존재하지 않는 과목입니다.")
            return_str += "들으실 강의가 존재하지 않는 과목입니다.\n"


# 과제 처리 부분
        return_str += "\n<과제> : \n"
        for i in range(len(temp_list)):
            res = session.post(temp_list[i], verify = False)
            soup = BeautifulSoup(res.text, "html.parser")
            temp_temp = soup.find("table", {"class": "bbsview"})
            temp_temp2 = soup.find("table", {"class" : "bbswrite"})
            # print(temp_temp)
            sub = temp_temp.text.split()
            print("temp2" , temp_temp2.text.split())
            print(sub)
            find_index = sub.index("마감일")
            find_index2 = sub.index("제출방식")
            # print(" ".join(sub[4 :find_index2]) , " 마감일 ", sub[find_index + 1: find_index + 3])
            if "제출일시" not in temp_temp2.text.split(): # 과제 제출 안함
                return_str += " ".join(sub[4 :find_index2]) + " 마감일 " + str(sub[find_index + 1: find_index + 3]) + "\n"
                # print(" ".join(sub[4 :find_index2]) , " 마감일 ", sub[find_index + 1: find_index + 3])

# 시험 처리 부분
        return_str += "\n<시험> : \n"
        for i in range(len(temp_list2)):
            res = session.post(temp_list2[i], verify = False)
            soup = BeautifulSoup(res.text, "html.parser")
            h = soup.find("tbody")
            # print(h.findAll("td"))
            h = h.findAll("td")
            li = []
            for j in range(len(h)):
                li.append(h[j].text)
            # print(li[:6])
            return_str += str(li[:6]) + "\n"


    return return_str
# a = get_session("201712672", "password")
# subject_list = get_subject_information()
# get_subject_details_information(subject_list)