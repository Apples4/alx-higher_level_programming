#!/usr/bin/node

const num = process.argv[2];

if (isNaN(parseInt(num))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(num); i++) {
    for (let j = 0; j < parseInt(num); j++) {
      process.stdout.write('x');
    }
  console.log()
  }
}
