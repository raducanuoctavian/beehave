window.onscroll = function() {onScroll()};
function onScroll() {
  if (document.body.scrollTop > 350 || document.documentElement.scrollTop > 350) {
    document.getElementById("navigation").style.backgroundColor = "white";
	var elements = document.getElementsByClassName("nav-link");
	for(var i = 0; i < elements.length; i++){
		elements[i].style.color = "black";
	}
  } else {
    document.getElementById("navigation").style.backgroundColor = "";
	var elements = document.getElementsByClassName("nav-link");
	for(var i = 0; i < elements.length; i++){
		elements[i].style.color = "";
  }
}}
