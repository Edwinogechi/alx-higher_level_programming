// Triggers the addition of an LI element to the list upon clicking the div#add_item tag
// The new element, <li>Item</li>, is appended to the UL.my_list

$('div#add_item').click(function () {
    // Create a new LI element with the text 'Item'
    let element = '<li>Item</li>';
    // Append the new element to the UL.my_list
    $('ul.my_list').append(element);
});
