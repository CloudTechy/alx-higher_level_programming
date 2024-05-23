#!/usr/bin/node
// display the status code of a GET request.

const req = require('request');
const url = process.argv[2];
req(url, (err, status) => {
  if (err) console.log(err);
  if (status) console.log("code:", status.statusCode);
});
