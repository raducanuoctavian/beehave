window.onscroll = function() {onScroll()};
function onScroll() {
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    document.getElementById("navigation").style.backgroundColor = "grey";
  } else {
    document.getElementById("navigation").style.backgroundColor = "transparent";
  }
}
