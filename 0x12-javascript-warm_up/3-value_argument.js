#!/usr/bin/node
// js script thatt prints the first argument passed to it
if (process.argv[2] != null) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
