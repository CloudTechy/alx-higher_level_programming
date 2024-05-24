#!/usr/bin/node
// output content of a webpage into a file.

const req = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

req(url, (err, status, body) => {
  if (err) console.log(err);
  if (status.statusCode === 200) {
    fs.writeFile(file, body, 'utf-8', (err) => {
      if (err) console.log(err);
    });
  }
});
