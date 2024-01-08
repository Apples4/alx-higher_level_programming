#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

if (process.argv.length <= 2) {
  console.log('NaN');
} else {
  console.log(a + b);
}
