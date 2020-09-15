#!/usr/bin/node
// My number: <first argument converted in integer> if the first argument can be converted to an integer
const num = parseInt(process.argv[2]);
if (Number.isInteger(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
