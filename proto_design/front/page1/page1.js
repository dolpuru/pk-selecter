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

function githubmove(){
  location.href ='https://github.com/doongu/pk_selecter_pj';
}
function gitbookmove(){
  location.href ='https://doongu.gitbook.io/pk_selecter/';
}
function page2(){
  location.href ='../page2/page2.html';
}
function loginmove() {
  document.getElementById("total").style.display = "none";
  document.getElementById("over").style.display = "block";
  document.body.style.backgroundColor = "white";
  document.body.style.lineHeight = "100px";
}
