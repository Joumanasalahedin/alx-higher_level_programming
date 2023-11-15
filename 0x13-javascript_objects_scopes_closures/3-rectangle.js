#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let c = 0; c < this.height; c++) {
      let row = '';
      for (let r = 0; r < this.width; r++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
