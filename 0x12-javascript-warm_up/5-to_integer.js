#!/usr/bin/node
// js script thatt prints My number: <first argument converted in integer>
if (!parseInt(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
