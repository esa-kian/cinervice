// dropdown 
$(document).ready(function() {
  $(".dropdown-toggle").dropdown();
});
// active class 
var test = document.getElementById('jeez');
test.onclick = function() {
    console.log('Hello');
}