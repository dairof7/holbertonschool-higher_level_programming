#!/usr/bin/node
// prints the number of arguments already printed and the new argument value
let count = 1;
exports.logMe = function (item) {
  console.log(count + ':' + item);
  count += 1;
};
