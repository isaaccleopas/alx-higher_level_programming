$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function (titles) {
  $("UL#list_movies").append(...titles.results.map(movie => `<li>${movie.title}</li>`));
});
