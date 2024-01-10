// Initiates a toggle on the class of the HTML 'HEADER' tag
// upon a user click event on the div#toggle_header element

$('div#toggle_header').click(function () {
    // Toggles the presence of the 'red' class on the 'header' tag
    $('header').toggleClass('red');
});
