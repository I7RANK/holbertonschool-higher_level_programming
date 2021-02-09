#!/usr/bin/node

const dadSquare = require('./5-square');

class Square extends dadSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let xStr = '';

    if (!c) {
      c = 'X';
    }

    for (let j = 0; j < this.width; j++) {
      xStr += c;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(xStr);
    }
  }
}

module.exports = Square;
