// Retrieves and updates the name from the API data, then substitutes
// the character's name within the text of the DIV#character tag

let apiUrl = 'https://swapi.co/api/people/5/?format=json';
$.get(apiUrl, function (responseData, status) {
  // Updates the text content of DIV#character with the fetched character's name
  $('div#character').text(responseData.name);
});
