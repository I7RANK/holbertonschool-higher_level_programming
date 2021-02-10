#!/usr/bin/node

$.get('https://swapi-api.hbtn.io/api/films/?format=json',
  function (data) {
    const movieTitles = data.results;
    console.log(movieTitles);

    for (let i = 0; i < movieTitles.length; i++) {
      $('UL#list_movies').append('<li>' + movieTitles[i].title + '</li>');
    }
  }
);
