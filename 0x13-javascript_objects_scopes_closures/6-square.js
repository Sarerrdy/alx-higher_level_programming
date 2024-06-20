#!/usr/bin/node

// Print function with custom characters to represent the Square

const parentSquare = require('./5-square');

module.exports = class Square extends parentSquare {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
