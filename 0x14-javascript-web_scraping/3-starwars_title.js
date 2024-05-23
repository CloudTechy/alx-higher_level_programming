#!/usr/bin/node
// display the status code of a GET request.

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
req(url + id + '/', (err, status, body) => {
  if (err) console.log(err);
  if (status.statusCode === 200) console.log(JSON.parse(body).title);
});
