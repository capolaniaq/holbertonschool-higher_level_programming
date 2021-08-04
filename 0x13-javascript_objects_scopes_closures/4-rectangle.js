#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((typeof w === 'number' && typeof h === 'number') && (w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let string = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        string = string + 'X';
      }
      console.log(string);
      string = '';
    }
  }

  double () {
    this.height = this.heighth * 2;
    this.width = this.width * 2;
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }
}
module.exports = Rectangle;
