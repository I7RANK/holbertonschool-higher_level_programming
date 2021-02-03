#!/usr/bin/node

let num = parseInt(process.argv[2]);
let neg = false;

if (num < 0) {
  num *= -1;
  neg = true;
}

function factorial (a) {
  if (!a) {
    return 1;
  }
  if (a > 1) {
    a *= factorial(a - 1);
  }
  return a;
}

num = factorial(num);

if (neg) {
  num *= -1;
}

console.log(num);
