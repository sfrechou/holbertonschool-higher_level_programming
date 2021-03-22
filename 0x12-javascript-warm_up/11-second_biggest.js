#!/usr/bin/node
// js script thatt searches the second biggest integer in the list of arguments
if (process.argv.length < 4) {
  console.log(1);
} else {
  const numbers = process.argv.slice(2);
  let biggest = 0;
  let secondBigg = 0;
  let i;
  for (i = 0; i < numbers.length; i++) {
    if (numbers[i] > biggest) {
      biggest = numbers[i];
    }
  }
  const indexBigg = numbers.indexOf(biggest);
  numbers.splice(indexBigg, 1);
  for (i = 0; i < numbers.length; i++) {
    if (numbers[i] > secondBigg) {
      secondBigg = numbers[i];
    }
  }
  console.log(secondBigg);
}
