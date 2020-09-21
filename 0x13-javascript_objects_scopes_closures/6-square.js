#!/usr/bin/node
// Square class that inhererit from Rectangle
// charPrint method that print the Square

const Rectangle = require('./5-rectangle');

module.exports = class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
};
