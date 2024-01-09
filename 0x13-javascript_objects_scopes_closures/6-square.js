#!/usr/bin/node
/**
 * Square that prints the rectangle using the character c
 */
const PrevSquare = require('./5-square.js');

class Square extends PrevSquare {
  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
          process.stdout.write('X');
        }
        console.log();
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
          process.stdout.write('C');
        }
        console.log();
      }
    }
  }
}

module.exports = Square;
