#!/usr/bin/node
// display the status code of a GET request
const request = require('request');

request(process.argv[2], function (response) {
  console.log('code:', response && response.statusCode); // Print the response status code if a response was received
});
