#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('x');
      }
      console.log();
    }
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    [this.height, this.width] = [this.height * 2, this.width * 2];
  }
};
