// dropdown 
$(document).ready(function() {
  $(".dropdown-toggle").dropdown();
});
// Active nav
$( document ).on( 'click', '.nav-list li', function ( e ) {
    $( this ).addClass( 'active' ).siblings().removeClass( 'active' );
} );