#!/usr/bin/node
/**
 * function that prints the number of arguments already printed
 */
let numberOfPrints = 0;

exports.logMe = function count (item) {
  console.log(`${numberOfPrints} : ${item}`);
  numberOfPrints = numberOfPrints + 1;
};
