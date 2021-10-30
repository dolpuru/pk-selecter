# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_session(lms_id, lms_pw):
    session = requests.Session()

    session_url = "https://lms.pknu.ac.kr/ilos/lo/login.acl"  # 세션을 얻을 url

    data = {"usr_id": lms_id, "usr_pwd": lms_pw}  # LMS 아이디  # LMS 비밀번호

    request = session.post(session_url, data=data, verify=False)
    confirm_login_soup = BeautifulSoup(request.text, "html.parser")

    # login_checker 에서 시행했음.
    # if "로그인 정보가 일치하지 않습니다." in confirm_login_soup.text:
    #     session.close()  # 세션 닫기
    #     return False
    return session


def Sub_subject_craw_module(session):

    subject_craw_url = (
        "https://lms.pknu.ac.kr/ilos/main/main_form.acl"  # 학수번호와 과목 명을 크롤링함
    )

    request = session.post(subject_craw_url, verify=False)
    sub_num_soup = BeautifulSoup(request.text, "html.parser")  # main에 요청보내서 학수번호 알아내기
    subject_list = sub_num_soup.findAll("em", {"sub", "sub_open"})

    return_subject_list = []
    for index in range(len(subject_list)):
        return_subject_list.append(
            [
                "".join(subject_list[index].text.replace(" ", "").split()),
                subject_list[index]["kj"],
            ]
        )

    return return_subject_list


def Sub_detail_sub_info(KJKEY, session):
    # global session

    craw_url = "https://lms.pknu.ac.kr/ilos/st/course/eclass_room2.acl"
    sub_main = "https://lms.pknu.ac.kr/ilos/st/course/submain_form.acl"
    data = {
        "KJKEY": KJKEY,  # n번째 과목의 학수번호
        "returnData": "json",
        "returnURI": "",
        "encoding": "utf-8",
    }

    request = session.post(craw_url, data=data, verify=False)  # 해당 과목에 대한 session을 얻는다.
    soup = BeautifulSoup(request.text, "html.parser")

    res = session.get(sub_main, verify=False)  # 해당 과목의 세션을 얻었을 때 url을 가져와야함

    soup = BeautifulSoup(res.text, "html.parser")
    right_banner = soup.find("div", {"class", "submain-rightarea"})  # 오른쪽 배너를 부르고

    detail_sub_info = right_banner.findAll("a", {"class", "site-link"})  # 부른 것에서 추출

    subject_url_list = []
    exam_url_list = []
    assignment_url = "https://lms.pknu.ac.kr"  # + "/ilos/st/course/report_view_form.acl?RT_SEQ=4057037" 과제는 그냥 get 때리면 됨, SEQ뒤에 과제 일렬번호 써줘야함

    # 오른쪽 부분을 이용해서 "과제와 시험기간이 현재 범위 인것만 긁는다."
    for i in range(len(detail_sub_info)):
        if "[과제]" in detail_sub_info[i].text.strip():
            subject_url_list.append(assignment_url + detail_sub_info[i]["href"])

        if "[시험]" in detail_sub_info[i].text.strip():
            exam_url_list.append(assignment_url + detail_sub_info[i]["href"])

    return subject_url_list, exam_url_list


def Sub_class_info(ky, session):

    online_list = "https://lms.pknu.ac.kr/ilos/st/course/online_list.acl"  # 수업

    data = {"ud": "", "ky": ky, "WEEK_NO": "", "encoding": "utf-8"}
    res = session.post(online_list, verify=False)

    soup = BeautifulSoup(res.text, "html.parser")
    temp_temp = soup.findAll("div", {"class", "lecture-box"})
    return temp_temp


def Sub_subject(craw_url, session):

    res = session.post(craw_url, verify=False)
    soup = BeautifulSoup(res.text, "html.parser")

    temp_temp = soup.find("table", {"class": "bbsview"})
    temp_temp2 = soup.find("table", {"class": "bbswrite"})

    return temp_temp, temp_temp2


def Sub_exam(craw_url, session):

    res = session.post(craw_url, verify=False)
    soup = BeautifulSoup(res.text, "html.parser")

    contents = soup.find("div", {"id": "contents"})
    return contents


def get_subject_information(lms_id, lms_pw):

    """
    세션 얻기
    """
    session = get_session(lms_id, lms_pw)

    """
    학수번호와 과목명을 크롤링
    """
    subject_list = Sub_subject_craw_module(session)

    """
    미완료 항목 크롤링
    """
    return_dic = {"status": 200, "subject": [], "lms_data": []}
    calender_form = {
        "subject_name": "",
        "class": "",
        "context": "",
        "date_deadline": "",
    }

    for index in range(len(subject_list)):
        return_dic["subject"].append(subject_list[index][0])  # json 추가부분

        # 수업 처리 부분

        temp_temp = Sub_class_info(subject_list[index][1], session)

        for i in range(len(temp_temp)):
            temp_list_find = temp_temp[i].text.split()

            if int(temp_list_find[-4][:-1]) < 100:
                index_ha = temp_list_find.index("학습인정기간")

                if "아닙니다." not in temp_list_find[:index_ha]:
                    calender_form["subject_name"] = subject_list[index][0]
                    calender_form["class"] = "수업"
                    calender_form["context"] = " ".join(temp_list_find[:index_ha])
                    calender_form["date_deadline"] = " ".join(
                        temp_list_find[index_ha + 6 : index_ha + 9]
                    )
                    return_dic["lms_data"].append(
                        dict(calender_form)
                    )  # dict해서 넣어야 이전값들이 안바뀜

        # 과제 및 시험 처리 부분

        # 과제 처리 부분

        temp_list, temp_list2 = Sub_detail_sub_info(subject_list[index][1], session)

        for i in range(len(temp_list)):

            temp_temp, temp_temp2 = Sub_subject(temp_list[i], session)

            sub = temp_temp.text.split()

            find_index = sub.index("마감일")
            find_index2 = sub.index("제출방식")

            if "제출일시" not in temp_temp2.text.split():  # 과제 제출 안함
                calender_form["subject_name"] = subject_list[index][0]
                calender_form["class"] = "과제"
                calender_form["context"] = " ".join(sub[4:find_index2])
                calender_form["date_deadline"] = " ".join(
                    sub[find_index + 1 : find_index + 4]
                )
                return_dic["lms_data"].append(dict(calender_form))

        # 시험 처리 부분
        for i in range(len(temp_list2)):
            h = Sub_exam(temp_list2[i], session)

            if "응시정보" in h.text:
                continue
            else:
                h = h.findAll("td")
                li = []
                for j in range(len(h)):
                    li.append(h[j].text)

                calender_form["subject_name"] = subject_list[index][0]
                calender_form["class"] = "시험"
                calender_form["context"] = li[0]
                calender_form["date_deadline"] = ", ".join(li[4:6])
                return_dic["lms_data"].append(dict(calender_form))

    session.close()
    return return_dic


# return_json = get_subject_information("201712672", "rlflsdPrh12#")
# print("return_json :: ", return_json)
