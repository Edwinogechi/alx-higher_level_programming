/* This script interacts with an API to retrieve and display translations for the greeting "Hello"
   based on the language code entered in the INPUT#language_code. */

$(document).ready(function () {
  // Ensure the document is fully loaded before handling user interactions

  // Attach a click event handler to the Translate button
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val(); // Extract the language code from the input

    // Initiate a GET request to fetch the translation
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${langCode}`, function (responseData) {
      // Update the content of the <div> with the fetched translation
      $('#hello').text(responseData.hello);
    });
  });
});
