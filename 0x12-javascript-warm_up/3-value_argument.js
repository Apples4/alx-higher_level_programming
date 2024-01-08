#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] === undefined) {
  console.log('No argument');
} else {
  for (let i = 2; i < argv.length; i++) {
    console.log(argv[i]);
  }
}
