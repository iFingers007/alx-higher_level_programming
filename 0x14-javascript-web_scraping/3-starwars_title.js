#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieApi = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.error('Error: Provide movie ID');
  process.exit(1);
}

request(movieApi, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.error('Failed to match Title');
  }
});
