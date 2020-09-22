#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
const char = 'https://swapi-api.hbtn.io/api/people/18/';
let count = 0;
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    for (let i = 0; i < data.count; i++) {
      for (let j = 0; j < data.results[i].characters.length; j++) {
        if (char === data.results[i].characters[j]) {
          count += 1;
          break;
        }
      }
    }
    console.log(count);
  }
});
