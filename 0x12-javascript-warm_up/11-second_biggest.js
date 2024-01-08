#!/usr/bin/node

const array = process.argv.slice(2);

if (process.argv.length <= 2) {
  console.log(0);
} else {
  array.sort((a, b) => b.length - a.length);
  console.log(array[1]);
}
