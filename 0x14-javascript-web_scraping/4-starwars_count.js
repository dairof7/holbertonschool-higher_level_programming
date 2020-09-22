#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    for (let i = 0; i < data.count; i++) {
      for (let j = 0; j < data.results[i].characters.length; j++) {
        if (data.results[i].characters[j].includes('/18/')) {
          count += 1;
          break;
        }
      }
    }
    console.log(count);
  }
});
