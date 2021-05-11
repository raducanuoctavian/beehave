window.onscroll = function() {onScroll()};
function onScroll() {
  if (document.body.scrollTop > 350 || document.documentElement.scrollTop > 350) {
    document.getElementById("navigation").style.backgroundColor = "#939b62";
  } else {
    document.getElementById("navigation").style.backgroundColor = "";
  }
}
