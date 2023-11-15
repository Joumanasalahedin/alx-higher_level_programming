#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let col = 0; col < this.height; col++) {
      let row = '';
      for (let r = 0; r < this.width; r++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
