$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    const list = $('#list_movies'); // Select the UL element using jQuery

    // Loop through each movie and append its title to the list
    movies.forEach(function (movie) {
      const listItem = $('<li></li>').text(movie.title);
      list.append(listItem);
    });
  }).fail(function () {
    console.error('Failed to get data');
  });
});
