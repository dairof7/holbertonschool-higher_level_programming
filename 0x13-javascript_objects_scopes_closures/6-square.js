#!/usr/bin/node
// Square class that inhererit from Rectangle
// charPrint method that print the Square

const Squaredad = require('./5-square');

module.exports = class Square extends Squaredad {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
