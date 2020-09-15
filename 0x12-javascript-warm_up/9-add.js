#!/usr/bin/node
// prints the addition of 2 integers

function add (a, b) {
  console.log(a + b);
}

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

if (Number.isInteger(num1) && Number.isInteger(num2)) {
  add(num1, num2);
} else {
  console.log('NaN');
}
