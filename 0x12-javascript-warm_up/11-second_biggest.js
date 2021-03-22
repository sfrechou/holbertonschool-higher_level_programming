#!/usr/bin/node
// js script thatt searches the second biggest integer in the list of arguments
if (process.argv.length < 4) {
  console.log(1);
} else {
  const numbers = process.argv.slice(2);
  let biggest = numbers[0];
  let secondBigg = numbers[0];
  let i;
  const negative = numbers.every(function (e) {
    return e < 0;
  });
  if (negative === true) {
    console.log('aqui');
    for (i = 0; i < numbers.length; i++) {
      if (numbers[i] < biggest) {
        biggest = numbers[i];
      }
    }
    const indexBigg = numbers.indexOf(biggest);
    numbers.splice(indexBigg, 1);
    for (i = 0; i < numbers.length; i++) {
      if (numbers[i] < secondBigg) {
        secondBigg = numbers[i];
      }
    }
  } else {
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
  }
  console.log(secondBigg);
}
