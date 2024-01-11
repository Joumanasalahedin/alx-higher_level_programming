const $ = window.$;
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  data.results.forEach(function (film) {
    $('#list_movies').append($('<li>').text(film.title));
  });
});
