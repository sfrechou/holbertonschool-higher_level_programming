#!/usr/bin/node
// js script thatt searches the second biggest integer in the list of arguments
if (process.argv.length < 4) {
  console.log(1);
} else {
  let numbers = process.argv.slice(2);
  numbers.sort(function (a, b) { return a - b; });
  let uniq = [...new Set(numbers)];
  let uniqNums = Array.from(uniq);
  let index = uniqNums.length;
  console.log(uniqNums[index - 2]);
}