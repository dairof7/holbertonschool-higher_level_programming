#!/usr/bin/node
// Square class that inhererit from Rectangle

module.exports = class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
};
