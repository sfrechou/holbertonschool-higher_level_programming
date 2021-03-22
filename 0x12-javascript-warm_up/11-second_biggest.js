#!/usr/bin/node
// js script thatt searches the second biggest integer in the list of arguments
if (process.argv.length < 4) {
  console.log(1);
} else {
  const numbers = process.argv.slice(2);
  numbers.sort(function (a, b) { return a - b; });
  const uniq = [...new Set(numbers)];
  const uniqNums = Array.from(uniq);
  const index = uniqNums.length;
  console.log(uniqNums[index - 2]);
}
