#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const actorId = '18';

if (!actorId) {
  console.error('Error: Provide movie ID');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    let count = 0;
    data.results.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${actorId}/`)) {
        count++;
      }
    });
    console.log(count);
  } else {
    console.error('Failed to retrieve films');
  }
});
