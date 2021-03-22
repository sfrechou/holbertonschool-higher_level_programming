#!/usr/bin/node
// js script thatt computes and prints a factorial
if (!parseInt(process.argv[2])) {
  console.log(1);
} else {
  const n = parseInt(process.argv[2]);
  function factorial (n) {
    if (n === 0) {
      return (1);
    }
    return n * factorial(n - 1);
  }
  console.log(factorial(n));
}
