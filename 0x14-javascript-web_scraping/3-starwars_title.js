#!/usr/bin/node
// Script that prints movie title
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  console.log(JSON.parse(body).title || err);
});
