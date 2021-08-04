#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let string = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        string = string + c;
      }
      console.log(string);
      string = '';
    }
  }
}
module.exports = Square;
