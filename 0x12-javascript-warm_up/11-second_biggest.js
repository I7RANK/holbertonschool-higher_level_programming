#!/usr/bin/node

/* similar to array[2:] in python */
let num = process.argv.slice(2);

// convert all index to int
num = num.map(i => parseInt(i));

function secondMax (list) {
  // the spread (...) may fail if the array is too long
  const max = Math.max(...num);
  let secondmax = Math.min(...num);

  for (const i in num) {
    if (num[i] > secondmax && num[i] < max) {
      secondmax = num[i];
    }
  }

  console.log(secondmax);
}

if (!num.length || num.length === 1) {
  console.log(0);
} else {
  secondMax(num);
}
