#!/usr/bin/node

var fs = require('fs');
let content = '';

fs.readFile(process.argv[2], function (err, data) {
  if (err) {
    return console.error(err);
  }
  add(data.toString() + '\n');
});

fs.readFile(process.argv[3], function (err, data) {
  if (err) {
    return console.error(err);
  }
  add(data.toString());
});

function add (data) {
  content += data;
  fs.writeFile(process.argv[4], content, function (err) {
    if (err) {
      return console.error(err);
    }
  });
}
