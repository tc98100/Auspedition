$(document).ready(function() {
    $( "#navbarS > li > a" ).bind( "click", function(event) {
        event.preventDefault();
        let clickedItem = $( this );
        $( "#navbarS > li > a" ).each( function() {
            $( this ).removeClass( "active" );
        });
        clickedItem.addClass( "active" );
    });
});