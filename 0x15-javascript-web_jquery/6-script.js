// Modifies the content of the header tag with a new header upon a click event
// Triggered when the DIV#update_header element is clicked

$('div#update_header').click(function () {
    // Sets the text of the 'header' tag to 'New Header!!!'
    $('header').text('New Header!!!');
});
