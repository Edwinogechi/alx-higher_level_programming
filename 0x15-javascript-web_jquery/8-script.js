// Initiates a request to an API, retrieves a list of movie titles, 
// and inserts them into the UL#list_movies tag

let apiUrl = 'https://swapi.co/api/films/?format=json';
$.get(apiUrl, function (responseData) {
  // Extracts the movie titles from the API response
  let movieTitles = responseData.results;
  // Appends each movie title to the UL#list_movies
  for (let title of movieTitles) {
    $('ul#list_movies').append(`<li>${title.title}</li>`);
  }
});
