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
document.getElementById("server_error").style.display = "none";

function githubmove() {
    location.href = 'https://github.com/doongu/pk_selecter_pj';
}

function gitbookmove() {
    location.href = 'https://doongu.gitbook.io/pk_selecter/';
}

function page1() {
    location.href = 'http://127.0.0.1:5002';
}


function loginmove() {
    document.getElementById("total").style.display = "none";
    document.getElementById("over").style.display = "block";
    document.body.style.backgroundColor = "white";
    document.body.style.lineHeight = "100px";

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
        .then(json => {
            if (json['status'] == 400) {
                document.getElementById("total").style.display = "block";
                document.getElementById("over").style.display = "none";
                document.body.style.backgroundColor = "rgba(0,0,0,0.1)";
                jQuery('#server_error').show();
                document.body.style.lineHeight = "1.6em";
                document.getElementById("server_error_inner").innerHTML = "비밀번호가 틀렸습니다. <br>다시 입력해 주세요 :)"

            } else if (json['status'] == 500) {
                document.getElementById("total").style.display = "block";
                document.getElementById("over").style.display = "none";
                document.body.style.backgroundColor = "rgba(0,0,0,0.1)";
                jQuery('#server_error').show();
                document.body.style.lineHeight = "1.6em";
                document.getElementById("server_error_inner").innerHTML = "서버 에러가 발생했습니다."
            } else if (json['status'] == 200) {
                class Deque {
                    constructor() {
                        this.arr = [];
                        this.head = 0;
                        this.tail = 0;
                    }

                    push_front(item) {
                        if (this.arr[0]) {
                            for (let i = this.arr.length; i > 0; i--) {
                                this.arr[i] = this.arr[i - 1];
                            }
                        }
                        this.arr[this.head] = item;
                        this.tail++;
                    }
                    push_back(item) {
                        this.arr[this.tail++] = item;
                    }
                    pop_front() {
                        if (this.head >= this.tail) {
                            return null;
                        } else {
                            const result = this.arr[this.head++];
                            return result;
                        }
                    }
                    pop_back() {
                        if (this.head >= this.tail) {
                            return null;
                        } else {
                            const result = this.arr[--this.tail];
                            return result;
                        }
                    }
                }

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

                const $calBody = document.querySelector('.cal-body');
                const $btnNext = document.querySelector('.btn-cal.next');
                const $btnPrev = document.querySelector('.btn-cal.prev');

                /**
                 * @param {number} date
                 * @param {number} dayIn
                 */

                function loadDate(date, dayIn) {
                    document.querySelector('.cal-day').textContent = date + " " + init.dayList[dayIn]
                }

                /**
                 * @param {date} fullDate
                 */

                let current_month;

                function loadYYMM(fullDate) {
                    let yy = fullDate.getFullYear();
                    let mm = fullDate.getMonth();
                    let firstDay = init.getFirstDay(yy, mm);
                    let lastDay = init.getLastDay(yy, mm);
                    let markToday; // for marking today date

                    if (mm === init.today.getMonth() && yy === init.today.getFullYear()) {
                        markToday = init.today.getDate();
                    }


                    document.querySelector('.cal-month').textContent = init.monList[mm];
                    current_month = mm + 1;
                    document.querySelector('.cal-year').textContent = yy;

                    let trtd = '';
                    let startCount;
                    let countDay = 0;
                    let circle_box = '';

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
                            if (countDay === lastDay.getDate()) {
                                startCount = 0;
                            }
                            trtd += circle_marked(countDay);
                            trtd += '</td>';
                        }
                        trtd += '</tr>';
                    }
                    $calBody.innerHTML = trtd;
                }

                function circle_marked(countDay) {
                    for (let j = 0; j < json['lms_data'].length; j++) {
                        let deadline_before = json['lms_data'][j]['date_deadline'];
                        let deadline_date = deadline_before.substr(8, 2);
                        let deadline_month = deadline_before.substr(5, 2);
                        if (deadline_date == countDay && deadline_month == current_month) {
                            return "<div id = circle1></div>";
                        }
                    }
                    return "<div id = circle2></div>";
                }

                let count = 0;

                function loadcontexts(date) {
                    let Content = new Array(1000)
                    for (let j = 0; j < json['lms_data'].length; j++) {
                        let deadline_before = json['lms_data'][j]['date_deadline'];
                        let deadline_date = deadline_before.substr(8, 2);
                        let deadline_month = deadline_before.substr(5, 2);
                        if (deadline_date == date && deadline_month == current_month) {
                            Content[j] = document.createElement('div');
                            Content[j].id = 'content'
                            let Subject_name = json['lms_data'][j]['subject_name'].split(']');
                            Content[j].innerHTML = json['lms_data'][j]['class'] + ": " + Subject_name[1] + "<br>" + json['lms_data'][j]['context'];
                            document.getElementById('Context-box').appendChild(Content[j]);
                            count++;
                        }
                    }
                    document.getElementById('Context-box').style.overflowY = "auto";
                }

                function removecontexts() {
                    if (count != 0) {
                        for (let i = 0; i < count; i++) {
                            let removecontext = document.getElementById('content');
                            removecontext.remove();
                        }
                    }
                    count = 0;
                }

                /**
                 * @param {string} val
                 */
                function createNewList(val) {
                    let id = new Date().getTime() + '';
                    let yy = init.activeDate.getFullYear();
                    let mm = init.activeDate.getMonth() + 1;
                    let dd = init.activeDate.getDate();
                    const $target = $calBody.querySelector(`.day[data-date="${dd}"]`);

                    let date = yy + '.' + init.addZero(mm) + '.' + init.addZero(dd);

                    let eventData = {};
                    eventData['date'] = date;
                    eventData['memo'] = val;
                    eventData['complete'] = false;
                    eventData['id'] = id;
                    init.event.push(eventData);
                    $todoList.appendChild(createLi(id, val, date));
                }

                loadYYMM(init.today);
                loadDate(init.today.getDate(), init.today.getDay());

                $btnNext.addEventListener('click', () => loadYYMM(init.nextMonth()));
                $btnPrev.addEventListener('click', () => loadYYMM(init.prevMonth()));

                // 날짜 눌렀을 때 !
                $calBody.addEventListener('click', (e) => {
                    if (e.target.classList.contains('day')) {
                        if (init.activeDTag) {
                            init.activeDTag.classList.remove('day-active');
                        }
                        let day = Number(e.target.textContent);
                        loadDate(day, e.target.cellIndex);
                        removecontexts();
                        loadcontexts(day);
                        e.target.classList.add('day-active');
                        init.activeDTag = e.target;
                        init.activeDate.setDate(day);
                        document.getElementById("clicked-date").style.display = "block";
                    }
                });


                let T = Array.from(Array(3), () => new Array(5));
                T[0][0] = "수업"
                T[0][1] = "수강 과목"
                T[0][2] = "강의 주차"
                T[0][3] = "마감 기한"
                T[0][4] = 'tableL';

                T[1][0] = "과제"
                T[1][1] = "수강 과목"
                T[1][2] = "과제내용"
                T[1][3] = "제출기한"
                T[1][4] = 'tableHW';

                T[2][0] = "시험"
                T[2][1] = "수강 과목"
                T[2][2] = "시험시간"
                T[2][3] = "제출기한"
                T[2][4] = 'tableT';




                /*======테이블=======*/
                let lms_data_json = new Array(json['lms_data'].length)

                for (let i = 0; i < json['lms_data'].length; i++) {
                    lms_data_json[i] = json['lms_data'][i]
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
                    list_sequence_deque[s] = new Deque
                    for (let i = 0; i < list_sequence[s].length; i++) {
                        list_sequence_deque[s].push_back(list_sequence[s][i])
                    }
                    len_deque[s] = list_sequence_deque[s]['arr'].length
                    answer[s] = new Array()

                    for (let i = 0; i < len_deque[s]; i++) {
                        let current_subject = list_sequence_deque[s].pop_front()
                        for (let j = 0; j < subject[s].length; j++) {
                            if (current_subject == subject[s][j]['subject_name']) {
                                answer[s].push(subject[s][j])
                            } else {
                                continue;
                            }
                        }
                    }
                }

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
                            document.getElementById(T[i][4]).appendChild(th[p]);
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
                        document.getElementById(T[i][4]).appendChild(row);
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
                                if (k == 0) {
                                    let Subject_name = answer[i][k]['subject_name'].split(']');
                                    td[k][0].innerHTML = Subject_name[1];
                                } else if (answer[i][k - 1]['subject_name'] == answer[i][k]['subject_name']) {
                                    td[k][0].innerHTML = "";
                                } else {
                                    let Subject_name = answer[i][k]['subject_name'].split(']');
                                    td[k][0].innerHTML = Subject_name[1];
                                }
                                if (answer[i][k]['class'] == '시험') {
                                    let Test_deadline_before = answer[i][k]['date_deadline'];
                                    let Test_deadline_after = Test_deadline_before.split(', ');
                                    td[k][1].innerHTML = Test_deadline_after[1];
                                    let deadline = Test_deadline_after[0].split(' ')
                                    td[k][2].innerHTML = deadline[0] + "<br>" + deadline[1] + " " + deadline[2];
                                } else {
                                    td[k][1].innerHTML = answer[i][k]['context'];
                                    let deadline = answer[i][k]['date_deadline'].split(' ')
                                    td[k][2].innerHTML = deadline[0] + "<br>" + deadline[1] + " " + deadline[2];
                                }
                                document.getElementById(T[i][4]).appendChild(row_1[k]);
                                for (let p = 0; p < 3; p++) {
                                    row_1[k].appendChild(td[k][p]);
                                }
                            }
                        }
                    }
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
            }

        })
}