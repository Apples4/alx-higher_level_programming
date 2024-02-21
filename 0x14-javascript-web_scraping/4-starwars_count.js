#!/usr/bin/node
//prints the number of movies where the character “Wedge Antilles” is present 
const request =  require('request');
const url = process.argv[2];


request(url, function (err, response, body) {
  if (err) console.log(err);
  let num = [];
  for (const film of JSON.parse(body).results) {
    num = num.concat(film.characters);
  }
  const uniq = num.filter(x => x.includes('18'));
    console.log(uniq.length);
})
