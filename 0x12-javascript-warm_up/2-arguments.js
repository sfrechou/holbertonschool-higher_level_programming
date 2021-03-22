#!/usr/bin/node
// js script thatt prints a message depending of the number of arguments passed
if (process.argv.length === 3) {
  console.log('Argument found');
} else if (process.argv.length < 3) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
