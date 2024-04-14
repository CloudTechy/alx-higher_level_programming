#!/usr/bin/node

const SquareC = require('./5-square.js');

class Square extends SquareC {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let h = this.height;
    while (h > 0) {
      console.log(c.repeat(this.width));
      h--;
    }
  }
}

module.exports = Square;
