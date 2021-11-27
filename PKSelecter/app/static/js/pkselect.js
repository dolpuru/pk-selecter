$(document).ready(function () {
    $(".form-panel.two")
        .not(".form-panel.two.active")
        .on("click", function (e) {
            e.preventDefault();
            $(".form-toggle").addClass("visible");
            $(".form-panel.two").addClass("hidden");
            $(".form-panel.two").addClass("active");
        });

    $(".form-toggle").on("click", function (e) {
        e.preventDefault();
        $(this).removeClass("visible");
        $(".form-panel.two").removeClass("hidden");
        $(".form-panel.two").removeClass("active");
    });
});

function githubmove() {
    location.href = 'https://github.com/doongu/pk_selecter_pj';
}

function gitbookmove() {
    location.href = 'https://doongu.gitbook.io/pk_selecter/';
}

function page1() {
    window.location.reload();
}

var delectBtnshow = 0;

function delectBtnonclick() {
    const delectBtn = document.querySelector('.delectBtn');
    if (delectBtnshow == 1) {
        delectBtn.innerHTML = "마감기한 지난 항목 삭제하기"
        delectBtnshow = 0;
    } else {
        delectBtn.innerHTML = "마감기한 지난 항목 확인하기"
        delectBtnshow = 1;
    }
    onclick();
}

var classfilterBtnshow = 0;

function classfilterBtnonclick() {
    const classfilterBtn = document.querySelector('.classfilterBtn');
    if (classfilterBtnshow == 1) {
        classfilterBtn.innerHTML = "과목 별로 보기"
        classfilterBtnshow = 0;
    } else {
        classfilterBtn.innerHTML = "강의, 과제, 시험 별로 보기"
        classfilterBtnshow = 1;
    }
    onclick();
}

function onclick() {
    if (delectBtnshow == 0 && classfilterBtnshow == 0) {
        $('.delectTabledata_subject').hide();
        $('.tabledata_subject').hide();
        $('.delectTabledata_catagory').hide();
        $('.tabledata_catagory').show();
    } else if (delectBtnshow == 1 && classfilterBtnshow == 0) {
        $('.delectTabledata_subject').hide();
        $('.tabledata_subject').hide();
        $('.delectTabledata_catagory').show();
        $('.tabledata_catagory').hide();
    } else if (delectBtnshow == 0 && classfilterBtnshow == 1) {
        $('.delectTabledata_subject').hide();
        $('.tabledata_subject').show();
        $('.delectTabledata_catagory').hide();
        $('.tabledata_catagory').hide();
    } else if (delectBtnshow == 1 && classfilterBtnshow == 1) {
        $('.delectTabledata_subject').show();
        $('.tabledata_subject').hide();
        $('.delectTabledata_catagory').hide();
        $('.tabledata_catagory').hide();
    }
}

var ddayBtnshow = 0;

function ddayBtnonclick() {
    const delectBtn = document.querySelector('.ddayBtn');
    if (ddayBtnshow == 1) {
        let Dday = getDday();
        delectBtn.style.backgroundColor = 'var(--color-white)';
        delectBtn.style.color = 'var(--color-black)';
        delectBtn.style.border = "2px solid var(--color-Basic-navy)";
        if (Dday >= 10) {
            delectBtn.innerHTML = `D - ${Dday}`;
        }else if(Dday == 0){
            delectBtn.innerHTML = `!! D - DAY !!`;
        }else if(Dday < 0){
            delectBtn.innerHTML = "!! Vacation !!";
        }else {
            delectBtn.innerHTML = `!! D - ${Dday} !!`;
        }
        ddayBtnshow = 0;
    } else {
        delectBtn.style.backgroundColor = 'var(--color-Basic-navy)';
        delectBtn.style.color = 'var(--color-white)';
        delectBtn.style.border = "0";
        delectBtn.innerHTML = "종강 D-Day";
        ddayBtnshow = 1;
    }
}

function getDday() {
    const vacation = new Date("2021-12-21:00:00:00+0900");
    const nowDay = new Date();
    const gap = vacation - nowDay
    const day = Math.floor(gap / (1000 * 60 * 60 * 24));
    const seconds = Math.floor((gap % (1000 * 60)) / 1000);
    let result = day + 1;
    return result;
}

function showLoadingPage() {
    document.getElementById("total").style.display = "none";
    document.getElementById("over").style.display = "block";
    document.body.style.backgroundColor = "white";
    document.body.style.lineHeight = "100px";
}

// status 값에 따른 에러처리
function alertError400() {
    document.getElementById("total").style.display = "block";
    document.getElementById("over").style.display = "none";
    document.body.style.backgroundColor = "#ebebeb";
    jQuery('#server_error').show();
    document.getElementById("server_error").style.display = "flex";
    document.body.style.lineHeight = "1.6em";
    document.getElementById("server_error_inner").innerHTML = "비밀번호가 틀렸습니다. <br>다시 입력해 주세요 :)"
}

function alertError500() {
    document.getElementById("total").style.display = "block";
    document.getElementById("over").style.display = "none";
    document.getElementById("server_error").style.display = "flex";
    document.body.style.backgroundColor = "#ebebeb";
    jQuery('#server_error').show();
    document.body.style.lineHeight = "1.6em";
    document.getElementById("server_error_inner").innerHTML = "서버 에러가 발생했습니다."
}

// 테이블 함수
function makeTableTitle() {
    let T = Array.from(Array(3), () => new Array(6));
    T[0][0] = "수업"
    T[0][1] = "수강 과목"
    T[0][2] = "강의 주차"
    T[0][3] = "마감 기한"
    T[0][4] = 'tabledata_tableL';
    T[0][5] = 'delectTabledata_tableL';

    T[1][0] = "과제"
    T[1][1] = "수강 과목"
    T[1][2] = "과제내용"
    T[1][3] = "제출기한"
    T[1][4] = 'tabledata_tableHW';
    T[1][5] = 'delectTabledata_tableHW';

    T[2][0] = "시험"
    T[2][1] = "수강 과목"
    T[2][2] = "시험시간"
    T[2][3] = "제출기한"
    T[2][4] = 'tabledata_tableT';
    T[2][5] = 'delectTabledata_tableT';

    return T;
}


function makeTableBonebycategory(datatype) {
    makeTableBonetablebycategory(datatype, "tableL", "미완료 강의");
    makeTableBonetablebycategory(datatype, "tableHW", "미제출 과제");
    makeTableBonetablebycategory(datatype, "tableT", "미제출 시험");
}

function makeTableBonebysubject(datatype, subject) {
    for (let i = 0; i < subject.length; i++) {
        makeTableBonetablebysubject(datatype, subject[i]);
    }
}

function makeTableBonetablebycategory(datatype, tabletype, tabletitle) {
    var table = document.createElement('table');
    table.id = `${datatype}_${tabletype}`;
    table.className = `${datatype}_catagory`;
    var tbody = document.createElement('tbody');
    var tr = document.createElement('tr');
    var th = document.createElement('th');
    th.id = "table_top";
    th.innerHTML = `${tabletitle}`;
    tr.appendChild(th);
    tbody.appendChild(tr);
    table.appendChild(tbody);
    document.querySelector(".tablebone").appendChild(table);
}

function makeTableBonetablebysubject(datatype, tabletitle) {
    var table = document.createElement('table');
    table.id = `${tabletitle}_${datatype}`;
    table.className = `${datatype}_subject`;
    var tbody = document.createElement('tbody');
    var tr = document.createElement('tr');
    let th = Array(4)
    th[0] = document.createElement('th');
    th[0].id = "table_top";
    let tabletitle_mid = tabletitle.split(']')[1];
    let tabletitle_after = tabletitle_mid.split('(');
    th[0].innerHTML = `${tabletitle_after[0]}<br>(${tabletitle_after[1]}`;
    tr.appendChild(th[0]);
    tbody.appendChild(tr);
    table.appendChild(tbody);
    document.querySelector(".tablebone").appendChild(table);
    th[1] = document.createElement('th');
    th[1].innerHTML = "항목";
    th[1].className = `th_${tabletitle}`;
    table.appendChild(th[1]);
    th[2] = document.createElement('th');
    th[2].innerHTML = "내용";
    th[2].className = `th_${tabletitle}`;
    table.appendChild(th[2]);
    th[3] = document.createElement('th');
    th[3].innerHTML = "마감 기한";
    th[3].className = `th_${tabletitle}`;
    table.appendChild(th[3]);
}

function loadsubjectTable(data, datatype) {
    let answer = arrangetablebysubject(data);
    showtablebysubject(answer, data['subject'], datatype)
}

function showtablebysubject(answer, subjectname, datatype) {
    for (let X = 0; X < subjectname.length; X++) {
        if (answer[X].length == 0) {
            let tr = document.createElement('tr');
            tr.innerHTML = "<td>모두 완료하셨습니다 :)</td>";
            document.getElementById(`${subjectname[X]}_${datatype}`).appendChild(tr);
            for (let i = 0; i < 6; i++) {
                document.getElementsByClassName(`th_${subjectname[X]}`)[i].style.display = "none";
            }
        } else {
            for (let i = 0; i < answer[X].length; i++) {
                let td = new Array(3);
                let tr = document.createElement('tr');
                document.getElementById(`${subjectname[X]}_${datatype}`).appendChild(tr);
                td[0] = document.createElement('td');
                td[0].innerHTML = answer[X][i]['class'];
                tr.appendChild(td[0]);
                td[1] = document.createElement('td');
                td[2] = document.createElement('td');
                if (answer[X][i]['class'] == '시험') {
                    let Test_deadline = answer[X][i]['date_deadline'].split(', ');
                    td[1].innerHTML = Test_deadline[1];
                    td[2].innerHTML = putthirdcolumn(Test_deadline[0]);
                } else {
                    td[1].innerHTML = answer[X][i]['context'];
                    td[2].innerHTML = putthirdcolumn(answer[X][i]['date_deadline']);
                }
                tr.appendChild(td[1]);
                tr.appendChild(td[2]);
            }
        }
    }
}


function arrangetablebysubject(data) {
    //날짜 순으로 정렬
    let sorteddata = data['lms_data'].sort((a, b) => {
        if (a['date_deadline'] > b['date_deadline']) {
            return 1;
        } else if (a['date_deadline'] < b['date_deadline']) {
            return -1;
        }
    })
    let answer = Array(data['subject'].length);
    for (let i = 0; i < data['subject'].length; i++) {
        for (let p = 0; p < sorteddata.length; p++) {
            answer[i] = sorteddata.filter(filterbysubject);

            function filterbysubject(item) {
                if (item['subject_name'] == data['subject'][i]) {
                    return true;
                }
                return false;
            }
        }
    }
    return answer;
}

function arrangetablebycategory(data) {
    let lms_data_json = new Array(data.length)

    for (let i = 0; i < data.length; i++) {
        lms_data_json[i] = data[i]
    }

    //강의, 과제, 시험 별로 분류
    let subject = new Array(3)

    for (let s = 0; s < 3; s++) {
        subject[s] = new Array(0)
    }

    for (let i = 0; i < lms_data_json.length; i++) {
        if (lms_data_json[i]['class'] == '수업') {
            subject[0].push(lms_data_json[i])
        } else if (lms_data_json[i]['class'] == '과제') {
            subject[1].push(lms_data_json[i])
        } else {
            subject[2].push(lms_data_json[i])
        }
    }

    //날짜 순으로 정렬
    for (let s = 0; s < 3; s++) {
        subject[s] = subject[s].sort((a, b) => {
            if (a['date_deadline'] > b['date_deadline']) {
                return 1;
            } else if (a['date_deadline'] < b['date_deadline']) {
                return -1;
            }
        })
    }

    let list_sequence = new Array(3);
    for (let s = 0; s < 3; s++) {
        list_sequence[s] = new Array(0);
        list_sequence[s] = subject[s].map(function (Subject_name) {
            // arr : subject_name만 추출
            return Subject_name['subject_name'];
        }).filter(function (Subject_name, index, arr) {
            // arr.indexOf(Subject_name): arr에 속하는 Subject_name의 인덱스가 
            // 지금 계산 중인 엔덱스와 같으면 반환
            return arr.indexOf(Subject_name) === index;
        });
    }

    let list_sequence_deque = new Array(3)
    let len_deque = new Array(3)
    let answer = new Array(3)
    for (let s = 0; s < 3; s++) {
        list_sequence_deque[s] = new Array(0);
        for (let i = 0; i < list_sequence[s].length; i++) {
            list_sequence_deque[s].push(list_sequence[s][i])
        }
        len_deque[s] = list_sequence_deque[s].length
        answer[s] = new Array()

        for (let i = 0; i < len_deque[s]; i++) {
            let current_subject = list_sequence_deque[s].shift()
            for (let j = 0; j < subject[s].length; j++) {
                if (current_subject == subject[s][j]['subject_name']) {
                    answer[s].push(subject[s][j])
                } else {
                    continue;
                }
            }
        }
    }
    return answer;
}



function showtablebycategory(answer, T, datatype,category) {

    let row_1 = new Array(10000);
    let row
    let th = new Array(3);
    // th ) 강의 과목 , 강의 주차, 마감기한 //
    for (let i = 0; i < 3; i++) {
        row_1[0] = document.createElement('tr');
        if (answer[i].length == 0) {
            row = document.createElement('tr');
            continue;
        } else {
            for (let p = 0; p < 3; p++) {
                th[p] = document.createElement('th');
                th[p].innerHTML = T[i][p + 1]
                document.getElementById(T[i][datatype]).appendChild(th[p]);
            }
        }
    }
    for (let i = 0; i < 3; i++) {
        //lms_data 길이 (열), 3행
        let td = Array.from(Array(answer[i].length), () => new Array(3));
        if (answer[i].length == 0) {
            let td1
            row = document.createElement('tr');
            td1 = document.createElement('td');
            td1.innerHTML = "모두 완료하셨습니다 :)";
            document.getElementById(T[i][datatype]).appendChild(row);
            row.appendChild(td1);
        } else {
            for (let k = 0; k < answer[i].length; k++) {
                if (answer[i][k]['class'] == T[i][0]) {
                    //행 제작
                    row_1[k] = document.createElement('tr');
                    // td 3개 제작 ( 강의 과목 , 강의 주차, 마감기한에 들어갈 칸 )
                    for (let p = 0; p < 3; p++) {
                        td[k][p] = document.createElement('td');
                    }

                    td[k][0].innerHTML = putfirstcolumn(k, answer[i]);

                    if (answer[i][k]['class'] == '시험') {
                        let Test_deadline_after = extractTestDeadline(answer[i][k]['date_deadline']);
                        td[k][1].innerHTML = Test_deadline_after[1];
                        td[k][2].innerHTML = putthirdcolumn(Test_deadline_after[0]);
                    } else {
                        td[k][1].innerHTML = answer[i][k]['context'];
                        td[k][2].innerHTML = putthirdcolumn(answer[i][k]['date_deadline']);
                    }

                    let today = getToday();
                    let compareanswertoday = answer[i][k]['date_deadline'].split(' ');
                    let middlestep = compareanswertoday[0].split('.');
                    let compareanswertomorrow = middlestep[0] + "." + middlestep[1] + "." + (parseInt(middlestep[2]) - 1);
                    if (today === compareanswertoday[0] || today === compareanswertomorrow) {
                        marktodayitem(td[k][1], td[k][2]);
                    }

                    document.getElementById(T[i][datatype]).appendChild(row_1[k]);
                    for (let p = 0; p < 3; p++) {
                        row_1[k].appendChild(td[k][p]);
                    }
                }
            }
        }
    }
}

function loadcatagoryTable(data, datatype, T,category) {
    let answer = arrangetablebycategory(data);
    showtablebycategory(answer, T, datatype,category);
}

function delectTabledata(data) {
    let today = getToday();
    let delectedData = new Array(0);
    for (let i = 0; i < data.length; i++) {
        let delectedDataDate = data[i]['date_deadline'].split(' ')[0];
        if (delectedDataDate >= today) {
            delectedData.push(data[i]);
        }
    }
    return delectedData;
}

function ShowSecondpage() {
    jQuery('#secondpage').show();
    jQuery('#mainpage').hide();
    let body = document.body;
    body.style.color = "rgba(0, 0, 0, 1)";
    body.style.backgroundColor = "rgba(0, 0, 0, 0.1)";
    body.style.fontWeight = "20";
    body.style.width = '100%';
    body.style.height = '100%';
    body.style.display = "inline";
    body.style.lineHeight = 'normal';
    let secondpage = document.getElementById("secondpage");
    secondpage.style.display = "flex";
}

function putfirstcolumn(k, category) {
    if (k == 0) {
        let Subject_name = category[k]['subject_name'].split(']');
        return Subject_name[1];
    } else if (category[k - 1]['subject_name'] == category[k]['subject_name']) {
        return "";
    } else {
        let Subject_name = category[k]['subject_name'].split(']');
        return Subject_name[1];
    }
}

function extractTestDeadline(date_deadline) {
    let Test_deadline = date_deadline.split(', ');
    return Test_deadline;
}

function putthirdcolumn(date_deadline) {
    let deadline = date_deadline.split(' ')
    return deadline[0] + "<br>" + deadline[1] + " " + deadline[2];
}

function getToday() {
    var date = new Date();
    var year = date.getFullYear();
    var month = ("0" + (1 + date.getMonth())).slice(-2);
    var day = ("0" + date.getDate()).slice(-2);

    return year + "." + month + "." + day;
}

function marktodayitem(task, date) {
    task.style.color = "red";
    task.style.fontWeight = "bold";
    date.style.color = "red";
    date.style.fontWeight = "bold";
}

function loginmove() {
    showLoadingPage();
    fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                pk_user_id: document.getElementById("username").value,
                pk_user_pw: document.getElementById("password").value,
            }),
        }).then((response => response.json()))
        .then(data => {
            if (data['status'] == 400) {
                alertError400();
            } else if (data['status'] == 500) {
                alertError500();
            } else if (data['status'] == 200) {
                // 달력 처음 값
                function loadInitCalender() {
                    const init = {
                        monList: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                        dayList: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
                        today: new Date(),
                        monForChange: new Date().getMonth(),
                        activeDate: new Date(),
                        getFirstDay: (yy, mm) => new Date(yy, mm, 1),
                        getLastDay: (yy, mm) => new Date(yy, mm + 1, 0),
                        nextMonth: function () {
                            let d = new Date();
                            d.setDate(1);
                            d.setMonth(++this.monForChange);
                            this.activeDate = d;
                            return d;
                        },
                        prevMonth: function () {
                            let d = new Date();
                            d.setDate(1);
                            d.setMonth(--this.monForChange);
                            this.activeDate = d;
                            return d;
                        },
                        addZero: (num) => (num < 10) ? '0' + num : num,
                        activeDTag: null,
                        getIndex: function (node) {
                            let index = 0;
                            while (node = node.previousElementSibling) {
                                index++;
                            }
                            return index;
                        }
                    };
                    return init;
                }

                const init = loadInitCalender();

                const calBody = document.querySelector('.cal-body');
                const btnNext = document.querySelector('.btn-cal.next');
                const btnPrev = document.querySelector('.btn-cal.prev');


                /**
                 * @param {number} date
                 * @param {number} dayIn
                 */
                // 달력 하단 박스에 클릭한 날의 월 일 요일 표시
                function loadDate(current_month, date, dayIn) {
                    document.querySelector('.cal-day').textContent = current_month + "월 " + date + "일 (" + init.dayList[dayIn] + ")";
                }


                let current_month;
                let current_year;
                /**
                 * @param {date} fullDate
                 */
                function loadYYMM(fullDate) {
                    // 달력에 보여지는 년도와 달
                    let yy = fullDate.getFullYear();
                    let mm = fullDate.getMonth();
                    // 해당 월의 첫 날과 마지막 날
                    let firstDay = init.getFirstDay(yy, mm);
                    let lastDay = init.getLastDay(yy, mm);
                    let markToday; // for marking today date

                    // 보여지는 달이 오늘의 년도와 달과 일치할 시 오늘의 날에 표시
                    if (mm === init.today.getMonth() && yy === init.today.getFullYear()) {
                        markToday = init.today.getDate();
                    }

                    // 캘린더 상단 bar에 년도와 달 표시
                    document.querySelector('.cal-month').textContent = init.monList[mm];
                    current_month = mm + 1;
                    document.querySelector('.cal-year').textContent = yy;

                    // 달력에 날짜 기입
                    function loadCalenderweeks() {
                        let trtd = '';
                        let upload_trtd = '';
                        let startCount;
                        let countDay = 0;
                        let tr_count = 0;

                        for (let i = 0; i < 6; i++) {

                            trtd += '<tr>';
                            for (let j = 0; j < 7; j++) {
                                if (i === 0 && !startCount && j === firstDay.getDay()) {
                                    startCount = 1;
                                }
                                if (!startCount) {
                                    trtd += '<td>';
                                } else {
                                    let fullDate = yy + '.' + init.addZero(mm + 1) + '.' + init.addZero(countDay + 1);
                                    trtd += '<td class="day';
                                    trtd += (markToday && markToday === countDay + 1) ? ' today" ' : '"';
                                    trtd += ` data-date="${countDay + 1}" data-fdate="${fullDate}">`;
                                }
                                trtd += (startCount) ? ++countDay : '';
                                trtd += circle_marked(countDay, yy, startCount);
                                if (countDay === lastDay.getDate()) {
                                    startCount = 0;
                                    tr_count++;
                                }
                                trtd += '</td>';
                            }
                            trtd += '</tr>';
                            if (tr_count <= 7) {
                                upload_trtd += trtd;
                                trtd = "";
                            }
                        }
                        calBody.innerHTML = upload_trtd;
                        current_year = yy;
                    }
                    loadCalenderweeks();
                }

                // 마감일에 해당하는 날 하늘색 다트로 표시하기
                function circle_marked(countDay, yy, startCount) {
                    for (let j = 0; j < data['lms_data'].length; j++) {
                        let deadline_before = data['lms_data'][j]['date_deadline'];
                        let deadline_date = deadline_before.substr(8, 2);
                        let deadline_month = deadline_before.substr(5, 2);
                        let deadline_year = deadline_before.substr(0, 4);
                        if (deadline_date == countDay && deadline_month == current_month && deadline_year == yy && startCount != 0) {
                            return "<div id = circle1></div>";
                        }
                    }
                    return "<div id = circle2></div>";
                }

                let count = 0;
                // 달력 하단 박스에 미제출 항목 표시
                function loadBoxContexts(date) {
                    let Content = new Array(1000);
                    count = 0;
                    for (let j = 0; j < data['lms_data'].length; j++) {
                        let deadline_before = data['lms_data'][j]['date_deadline'];
                        let deadline_date = deadline_before.substr(8, 2);
                        let deadline_month = deadline_before.substr(5, 2);
                        let deadline_year = deadline_before.substr(0, 4);
                        if (deadline_date == date && deadline_month == current_month && deadline_year == current_year) {
                            Content[j] = document.createElement('div');
                            Content[j].id = 'content'
                            let Subject_name = data['lms_data'][j]['subject_name'].split(']');
                            Content[j].innerHTML = data['lms_data'][j]['class'] + ": " + Subject_name[1] + "<br>" + data['lms_data'][j]['context'];
                            document.querySelector('#Context-box').appendChild(Content[j]);
                            count++;
                        }
                    }
                    document.querySelector("#clicked-date").style.display = "block";
                    if (count == 0) {
                        document.querySelector("#content-nonebox").style.display = "block";
                    }

                }
                // 다른 날짜 클릭시 달력 하단 박스에 미제출 항목 삭제
                function removeBoxContexts() {
                    if (count != 0) {
                        for (let i = 0; i < count; i++) {
                            let removecontext = document.querySelector('#content');
                            removecontext.remove();
                        }
                    }
                    document.querySelector("#content-nonebox").style.display = "none";
                    count = 0;
                }

                /**
                 * @param {string} val
                 */
                //처음 secondpage 왔을 때 오늘의 날 load
                loadYYMM(init.today);
                // 캘린더 상단의 월 이동 버튼을 눌렀을 때
                btnNext.addEventListener('click', () => loadYYMM(init.nextMonth()));
                btnPrev.addEventListener('click', () => loadYYMM(init.prevMonth()));

                // 달력의 날짜 눌렀을 때 !
                calBody.addEventListener('click', (e) => {
                    if (e.target.classList.contains('day')) {
                        if (init.activeDTag) {
                            init.activeDTag.classList.remove('day-active');
                        }
                        let day = Number(e.target.textContent);
                        loadDate(current_month, day, e.target.cellIndex);
                        removeBoxContexts();
                        loadBoxContexts(day);
                        e.target.classList.add('day-active');
                        init.activeDTag = e.target;
                        init.activeDate.setDate(day);
                    }
                });

                /*======테이블=======*/
                let T = makeTableTitle();
                let tabledata = data['lms_data'];

                let delectedData = delectTabledata(tabledata);

                makeTableBonebycategory("tabledata");
                makeTableBonebycategory("delectTabledata");
                loadcatagoryTable(tabledata, 4, T,"tabledata");
                loadcatagoryTable(delectedData, 5, T,"delectTabledata");


                makeTableBonebysubject("tabledata", data['subject']);
                makeTableBonebysubject("delectTabledata", data['subject']);
                loadsubjectTable(data, "tabledata");
                let delected_lms_Data = {
                    lms_data: delectedData,
                    status: 200,
                    subject: data['subject']
                };
                loadsubjectTable(delected_lms_Data, "delectTabledata");
                ShowSecondpage();
            }
        })
}