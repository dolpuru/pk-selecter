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
function githubmove(){
  location.href ='https://github.com/doongu/pk_selecter_pj';
}
function gitbookmove(){
  location.href ='https://doongu.gitbook.io/pk_selecter/';
}
function page1(){
  //첫페이지 링크 걸기
  location.href = 'http://127.0.0.1:5501/pkselect.html';
}
function page2(){
      jQuery('#secondpage').show();
      jQuery('#mainpage').hide();
      let body = document.body;
      body.style.color="rgba(0, 0, 0, 1)";   
      body.style.backgroundColor= "rgba(0, 0, 0, 0.1)";
      body.style.fontWeight = "20";
      body.style.width = '100%';
      body.style.height = '100%';
      body.style.display = "inline";
      body.style.lineHeight = 'normal';
      let secondpage = document.getElementById("secondpage");
      secondpage.style.display = "flex";
}
function loginmove() {
  document.getElementById("total").style.display = "none";
  document.getElementById("over").style.display = "block";
  document.body.style.backgroundColor = "white";
  document.body.style.lineHeight = "100px";
}

fetch("/login", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    pk_user_id : "201712672",
    pk_user_pw : "rlflsdPrh12#",
  }),
}).then((response => response.json()))
.then(json => { 
     if(json['status'] == 200){
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
var T = Array.from(Array(3), () => new Array(5));
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

for(let i = 0; i < json['lms_data'].length ; i++){
lms_data_json[i] = Object.values(json['lms_data'][i])
}

//강의, 과제, 시험 별로 분류
let subject = new Array(3)
for(let s = 0; s<3;s++){
subject[s] = new Array(0)
}

for(let i = 0; i < lms_data_json.length ; i++){
if(lms_data_json[i][1]=='수업'){
  subject[0].push(lms_data_json[i])
}else if(lms_data_json[i][1]=='과제'){
  subject[1].push(lms_data_json[i])
}else{
  subject[2].push(lms_data_json[i])
}
}

//날짜 순으로 정렬
for(let s = 0; s<3;s++){
subject[s] = subject[s].sort((a, b) => {
if (a[3] > b[3]) {
    return 1;
} else if (a[3] < b[3]) {
    return -1;
} 
})
}

let list_sequence = new Array(3);
for(let s = 0; s<3;s++){
list_sequence[s] = new Array(0);
for(let i = 0 ; i <subject[0].length;i++){
result = list_sequence[s].toString().indexOf(subject[0][i][0]);
if(result >= 0){
}else{
  list_sequence[s].push(subject[0][i][0])
}
}
}


let list_sequence_deque = new Array(3)
let len_deque = new Array(3)
let answer = new Array(3)
for(let s = 0; s<3;s++){
list_sequence_deque[s] = new Deque
for(let i = 0 ; i< list_sequence[0].length;i++){
list_sequence_deque[s].push_back(list_sequence[s][i])
}
len_deque[s] = list_sequence_deque[0]['arr'].length
answer[s]= new Array()

for(let i = 0; i < len_deque[s];i++){
let current_subject =list_sequence_deque[s].pop_front()
for(let j = 0; j < subject[s].length; j++){
  if(current_subject == subject[s][j][0]){
    answer[s].push(subject[s][j])
  }else{
    continue;
  }
}
}
}
var row_1 = new Array(10000);
var th = new Array(3);
// th ) 강의 과목 , 강의 주차, 마감기한 //
for(var i = 0; i < 3; i++){
  row_1[0] = document.createElement('tr');
  for (var p = 0; p < 3; p++) {
    th[p] = document.createElement('th');
    th[p].innerHTML = T[i][p + 1]
    document.getElementById(T[i][4]).appendChild(th[p]);
  }
} 

  for(var i = 0; i < 3; i++){
    //lms_data 길이 (열), 3행
    var td = Array.from(Array(answer[0].length), () => new Array(3));
    for(let k = 0 ; k<answer[i].length;k++){
    if(answer[i][k][1] == T[i][0]){
      //행 제작
      row_1[k] = document.createElement('tr');
      // td 3개 제작 ( 강의 과목 , 강의 주차, 마감기한에 들어갈 칸 )
      for (var p = 0; p < 3; p++) {
        td[k][p] = document.createElement('td');
      }
      if(k == 0){
      td[k][0].innerHTML = answer[i][k][0];
      }else if(answer[i][k-1][0]== answer[i][k][0]){
        td[k][0].innerHTML = "";
      }else{
        td[k][0].innerHTML = answer[i][k][0];
      }
      if(answer[i][k][1] == '시험'){
        var Test_deadline_before = answer[i][k][3];
        var Test_deadline_after = Test_deadline_before.split(', ');
        td[k][1].innerHTML = Test_deadline_after[1];
        td[k][2].innerHTML = Test_deadline_after[0];
      }else{
      td[k][1].innerHTML = answer[i][k][2];
      td[k][2].innerHTML = answer[i][k][3];
      }
      document.getElementById(T[i][4]).appendChild(row_1[k]);
      for (var p = 0; p < 3; p++) {
        row_1[k].appendChild(td[k][p]);
      }
    }
    }
  }

}else if(json['status']== 400){
  jQuery('#server_error').show();
  document.getElementById("server_error_inner").innerHTML = "비밀번호가 틀렸습니다. <br>다시 입력해 주세요 :)"
  }else if(json['status']== 500){
    jQuery('#server_error').show();
    document.getElementById("server_error_inner").innerHTML ="서버 에러가 발생했습니다."
  }

   })

//테이블//
// var json = 
//     {
//       "status": 200,
//       "subject": [
//         "[가상]과제구현및평가(캡스톤디자인Ⅱ)(105)",
//         "[가상]데이터베이스(101)",
//         "[가상]데이터베이스응용(102)",
//         "[가상]데이터처리Ⅱ(102)",
//         "[가상]리눅스프로그래밍(101)",
//         "[가상]소프트웨어공학(102)",
//         "[가상]시스템프로그래밍(102)",
//         "[가상]프로그래밍언어론(101)",
//         "[부경대]2021RUN&LEARN부경팀프로젝트(01)"
//       ],
//       "lms_data": [
//         {
//           "subject_name": "[가상]시스템프로그래밍(102)",
//           "class": "수업",
//           "context": "1차시 write() System Call",
//           "date_deadline": "2021.10.13 오후 11:59"
//         },
//         {
//           "subject_name": "[가상]과제구현및평가(캡스톤디자인Ⅱ)(105)",
//           "class": "과제",
//           "context": "학술발표논문제출(10월17일까지)",
//           "date_deadline": "2021.10.17 오후 11:59"
//         },
//         {
//           "subject_name": "[가상]데이터베이스(101)",
//           "class": "수업",
//           "context": "1차시 DB01-1",
//           "date_deadline": "2021.09.07 오후 11:59"
//         },
//         {
//           "subject_name": "[가상]데이터베이스응용(102)",
//           "class": "수업",
//           "context": "1차시 교재 5 장. ER을 이용한 데이터 모델링 (이론부분)",
//           "date_deadline": "2021.10.12 오후 11:59"
//         },
//         {
//           "subject_name": "[가상]데이터베이스응용(102)",
//           "class": "수업",
//           "context": "2차시 교재 3~4장 복습 (실습부분)",
//           "date_deadline": "2021.10.12 오후 11:59"
//         },
//         {
//           "subject_name": "[가상]데이터베이스응용(102)",
//           "class": "수업",
//           "context": "3차시 교재 3~4장 복습 (실습부분)",
//           "date_deadline": "2021.10.12 오후 11:59"
//         },
//         {
//           "subject_name": "[가상]데이터베이스응용(102)",
//           "class": "과제",
//           "context": "6주차 과제",
//           "date_deadline": "2021.10.13 오후 11:59"
//         },
//         {
//           "subject_name": "[가상]데이터베이스응용(102)",
//           "class": "시험",
//           "context": "5장 정리 퀴즈",
//           "date_deadline": "2021.10.13 오후 11:59, 10분"
//         },
//         {
//           "subject_name": "[가상]리눅스프로그래밍(101)",
//           "class": "수업",
//           "context": "1차시 3장 파일과 디렉토리 (1)",
//           "date_deadline": "2021.10.18 오후 11:59"
//         },
//         {
//           "subject_name": "[가상]리눅스프로그래밍(101)",
//           "class": "과제",
//           "context": "3장 파일과 디렉토리 (1)",
//           "date_deadline": "2021.10.17 오후 11:59"
//         },
//         {
//           "subject_name": "[가상]시스템프로그래밍(102)",
//           "class": "수업",
//           "context": "2차시 Delayed writing",
//           "date_deadline": "2021.10.13 오후 11:59"
//         },
//         {
//           "subject_name": "[가상]시스템프로그래밍(102)",
//           "class": "수업",
//           "context": "5주 3차시 보강 I/O Synchronization",
//           "date_deadline": "2021.10.13 오후 11:59"
//         },
//         {
//           "subject_name": "[가상]프로그래밍언어론(101)",
//           "class": "과제",
//           "context": "프로그래밍언어론 Assignment#1",
//           "date_deadline": "2021.10.13 오후 11:59"
//         }
//       ]
//     }; 

      