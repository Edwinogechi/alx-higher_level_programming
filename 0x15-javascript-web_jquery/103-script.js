/* This script interacts with an external API to retrieve and display translations for the greeting "Hello"
   based on the language code entered by the user when the Translate button is clicked or the Enter key is pressed. */

$(document).ready(function () {
  // Ensure the document is fully loaded before handling user interactions

  // Function to initiate the translation fetching and display
  function fetchAndDisplayTranslation() {
    // Extract the language code entered by the user
    const languageCode = $('#language_code').val();

    // Make a GET request to fetch the translation
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (responseData) {
      // Update the content of the HTML tag DIV#hello with the fetched translation
      $('#hello').text(responseData.hello);
    });
  }

  // Attach a click event handler to the Translate button
  $('#btn_translate').click(fetchAndDisplayTranslation);

  // Attach a keypress event handler to the language code input field
  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      // Check if the Enter key is pressed (keyCode 13)
      fetchAndDisplayTranslation();
    }
  });
});
