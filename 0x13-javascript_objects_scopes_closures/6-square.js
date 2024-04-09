#!/usr/bin/node

const SquareC = require('./5-square.js');

class Square extends SquareC {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c) {
      let h = this.height;
      while (h > 0) {
        console.log(c.repeat(this.width));
        h--;
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
