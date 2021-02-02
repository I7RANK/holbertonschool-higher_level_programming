#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial (a, b = 1) {
  if (a > 1) {
    b *= a;
    b = factorial(a - 1, b);
  }
  return b;
}

console.log(factorial(num));
