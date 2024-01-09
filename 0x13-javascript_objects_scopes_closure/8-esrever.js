#!/usr/bin/node
/**
 * function that returns the reversed version of a list
 */
exports.esrever = function (list) {
  const reverseOrder = [];

  for (let i = list.length - 1; i >= 0; i--) {
    reverseOrder.push(list[i]);
  }
  return (reverseOrder);
};
