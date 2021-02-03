#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial (a) {
  if (a > 1) {
    a *= factorial(a - 1);
  }
  return a;
}

console.log(factorial(num));
