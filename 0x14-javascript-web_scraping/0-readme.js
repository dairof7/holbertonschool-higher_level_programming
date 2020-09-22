#!/usr/bin/node
// Read a file and print the content
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (data, err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data.toString().trim());
  }
});
