#!/usr/bin/node
// display the counted character of a GET request.

const req = require('request');
const url = process.argv[2];
req(url, (err, status, body) => {
  if (err) console.log(err);
  if (status.statusCode === 200) {
    let sum = 0;
    const castUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
    const films = JSON.parse(body);
    for (const film of films.results) {
      if (film.characters && film.characters.includes(castUrl)) sum++;
    }
    console.log(sum);
  }
});
