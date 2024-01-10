/* This script manages the dynamic manipulation of LI elements within a list,
   responding to user interactions by adding, removing, or clearing items. */

$(document).ready(function () {
  // Ensure the document is fully loaded before handling user events

  // Incorporate a new <li> element into the list within UL.my_list
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  // Eliminate the last <li> element from the list within UL.my_list
  $('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  // Eliminate all <li> elements from the list within UL.my_list
  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
