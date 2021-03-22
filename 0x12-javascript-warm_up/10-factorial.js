#!/usr/bin/node
// js script thatt computes and prints a factorial

const n = parseInt(process.argv[2]);
function factorial (n) {
  if (isNaN(n) === true) {
    return (1);
  } else {
    if (n === 0) {
      return (1);
    }
    return (n * factorial(n - 1));
  }
}
console.log(factorial(n));
