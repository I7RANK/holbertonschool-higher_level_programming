#!/usr/bin/node

const Cisfun = 'C is fun';
const num = parseInt(process.argv[2]);
let i;

if (num) {
  for (i = 0; i < num; i++) {
    console.log(Cisfun);
  }
} else {
  console.log('Missing number of occurrences');
}
