#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file
const fs = require('fs');
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) console.log(err);
  fs.write(process.argv[3], body, err => {
    if (err) console.log(err);
  });
});
