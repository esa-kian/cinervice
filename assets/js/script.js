// dropdown 
$(document).ready(function() {
  $(".dropdown-toggle").dropdown();
});
// Active nav
$(document).ready(function() {
  $('a[href$="' + location.pathname + '"]').addClass('active');
});