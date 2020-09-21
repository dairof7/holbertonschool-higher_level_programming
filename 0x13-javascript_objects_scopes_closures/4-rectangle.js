#!/usr/bin/node
// Rectangle class with height and width
// print method to print the rectangle
// rotate method that exchanges the width and the height
// double method that multiples the width and the height
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const str = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(str.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
