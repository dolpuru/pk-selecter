# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 보통 비상수 값은 global로 잘 정의하지 않지만 아래 모든 함수가 session을 사용하기에 global로 선언해주었다.
session = requests.Session()


def get_session(lms_id, lms_pw):
    global session

    session_url = "https://lms.pknu.ac.kr/ilos/lo/login.acl"  # 세션을 얻을 url

    data = {"usr_id": lms_id, "usr_pwd": lms_pw}  # LMS 아이디  # LMS 비밀번호

    request = session.post(session_url, data=data, verify=False)
    confirm_login_soup = BeautifulSoup(request.text, "html.parser")

    if "로그인 정보가 일치하지 않습니다." in confirm_login_soup.text:
        session.close()  # 세션 닫기
        return False

    else:
        return True


def get_subject_information():
    global session

    return_subject_list = []

    subject_craw_url = (
        "https://lms.pknu.ac.kr/ilos/main/main_form.acl"  # 학수번호와 과목 명을 크롤링함
    )

    request = session.post(subject_craw_url, verify=False)
    sub_num_soup = BeautifulSoup(request.text, "html.parser")  # main에 요청보내서 학수번호 알아내기
    temp_subject_list = sub_num_soup.findAll("em", {"sub", "sub_open"})

    for index in range(len(temp_subject_list)):
        return_subject_list.append(
            [
                "".join(temp_subject_list[index].text.replace(" ", "").split()),
                temp_subject_list[index]["kj"],
            ]
        )

    return return_subject_list


def get_subject_details_information(subject_list):
    global session

    return_dic = {"status": 200, "subject": [], "lms_data": []}
    calender_form = {
        "subject_name": "",
        "class": "",
        "context": "",
        "date_deadline": "",
    }

    return_str = ""
    craw_url = "https://lms.pknu.ac.kr/ilos/st/course/eclass_room2.acl"
    sub_main = "https://lms.pknu.ac.kr/ilos/st/course/submain_form.acl"
    online_list = "https://lms.pknu.ac.kr/ilos/st/course/online_list.acl"  # 수업
    # + "/ilos/st/course/report_view_form.acl?RT_SEQ=4057037" 과제는 그냥 get 때리면 됨, SEQ뒤에 과제 일렬번호 써줘야함
    assignment_url = "https://lms.pknu.ac.kr"

    for index in range(len(subject_list)):
        data = {
            "KJKEY": subject_list[index][1],  # n번째 과목의 학수번호
            "returnData": "json",
            "returnURI": "",
            "encoding": "utf-8",
        }

        # 해당 과목에 대한 session을 얻는다.
        request = session.post(craw_url, data=data, verify=False)
        soup = BeautifulSoup(request.text, "html.parser")

        # 해당 과목의 세션을 얻었을 때 url을 가져와야함
        res = session.get(sub_main, verify=False)

        soup = BeautifulSoup(res.text, "html.parser")
        temp_right = soup.find("div", {"class", "submain-rightarea"})  # 오른쪽 배너를 부르고
        temp_detail_sub_info = temp_right.findAll(
            "a", {"class", "site-link"}
        )  # 부른 것에서 추출

        # 강의랑 과제만뽑아야함
        return_str += "===" * 35 + "\n"
        print("===" * 35)
        return_str += "과목명 : " + subject_list[index][0] + "\n"
        print("과목명 : " + subject_list[index][0] + "\n")
        return_dic["subject"].append(subject_list[index][0])  # json 추가부분

        temp_list = []
        temp_list2 = []

        # 오른쪽 부분을 이용해서 "과제와 시험기간이 현재 범위 인것만 긁는다."
        for i in range(len(temp_detail_sub_info)):
            if "[과제]" in temp_detail_sub_info[i].text.strip():

                temp_list.append(assignment_url + temp_detail_sub_info[i]["href"])
            if "[시험]" in temp_detail_sub_info[i].text.strip():
                temp_list2.append(assignment_url + temp_detail_sub_info[i]["href"])

        # 수업 처리 부분
        print("<수업> : \n")
        return_str += "<수업> : \n"
        try:
            data = {
                "ud": "",
                "ky": subject_list[index][1],
                "WEEK_NO": "",
                "encoding": "utf-8",
            }
            res = session.post(online_list, verify=False)

            soup = BeautifulSoup(res.text, "html.parser")
            temp_temp = soup.findAll("div", {"class", "lecture-box"})
            for i in range(len(temp_temp)):
                temp_list_find = temp_temp[i].text.split()
                # print(temp_list_find)
                if int(temp_list_find[-4][:-1]) < 100:
                    index_ha = temp_list_find.index("학습인정기간")
                    if "아닙니다." not in temp_list_find[:index_ha]:
                        return_str += (
                            str(temp_list_find[:index_ha])
                            + " "
                            + str(temp_list_find[index_ha + 6 : index_ha + 9])
                            + " "
                            + "까지 수강을 완료하셔야합니다.\n"
                        )
                        print(
                            temp_list_find[:index_ha],
                            temp_list_find[index_ha + 6 : index_ha + 9],
                            "까지 수강을 완료하셔야합니다.",
                        )
                        # print(temp_list_find)
                        calender_form["subject_name"] = subject_list[index][0]
                        calender_form["class"] = "수업"
                        calender_form["context"] = " ".join(temp_list_find[:index_ha])
                        calender_form["date_deadline"] = " ".join(
                            temp_list_find[index_ha + 6 : index_ha + 9]
                        )
                        return_dic["lms_data"].append(
                            dict(calender_form)
                        )  # dict해서 넣어야 이전값들이 안바뀜
        except:
            print("들으실 강의가 존재하지 않는 과목입니다.")
            return_str += "들으실 강의가 존재하지 않는 과목입니다.\n"

        # 과제 처리 부분
        print("\n<과제> : \n")
        return_str += "\n<과제> : \n"
        for i in range(len(temp_list)):
            res = session.post(temp_list[i], verify=False)
            soup = BeautifulSoup(res.text, "html.parser")
            temp_temp = soup.find("table", {"class": "bbsview"})
            temp_temp2 = soup.find("table", {"class": "bbswrite"})
            # print(temp_temp)
            sub = temp_temp.text.split()
            # print("temp2" , temp_temp2.text.split())
            print("sub: ", sub)
            find_index = sub.index("마감일")
            find_index2 = sub.index("제출방식")
            if "제출일시" not in temp_temp2.text.split():  # 과제 제출 안함
                return_str += (
                    " ".join(sub[4:find_index2])
                    + " 마감일 "
                    + str(sub[find_index + 1 : find_index + 3])
                    + "\n"
                )
                print(
                    " ".join(sub[4:find_index2]),
                    " 마감일 ",
                    sub[find_index + 1 : find_index + 3],
                )

                calender_form["subject_name"] = subject_list[index][0]
                calender_form["class"] = "과제"
                calender_form["context"] = " ".join(sub[4:find_index2])
                calender_form["date_deadline"] = " ".join(
                    sub[find_index + 1 : find_index + 4]
                )
                return_dic["lms_data"].append(dict(calender_form))

        # 시험 처리 부분
        print("\n<시험> : \n")
        return_str += "\n<시험> : \n"
        for i in range(len(temp_list2)):
            res = session.post(temp_list2[i], verify=False)
            soup = BeautifulSoup(res.text, "html.parser")
            h = soup.find("div", {"id": "contents"})
            print(h.text)
            if "응시정보" in h.text:
                continue
            # print(h)
            h = h.findAll("td")

            li = []
            for j in range(len(h)):
                li.append(h[j].text)
            print(li)
            return_str += str(li[:6]) + "\n"
            calender_form["subject_name"] = subject_list[index][0]
            calender_form["class"] = "시험"
            calender_form["context"] = li[0]
            calender_form["date_deadline"] = ", ".join(li[4:6])
            return_dic["lms_data"].append(dict(calender_form))
    return return_dic


# get_session("201712672", "rlflsdPrh12#")
# subject_list = get_subject_information()

# return_json = get_subject_details_information(subject_list)
# z = json.dumps(return_json, indent=2, ensure_ascii=False)
# print(z)
