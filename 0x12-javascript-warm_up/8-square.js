#!/usr/bin/node
// js script thatt prints a square
let i, j;
if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  for (i = 0; i < parseInt(process.argv[2]); i++) {
    for (j = 0; j < parseInt(process.argv[2]); j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
