#!/usr/bin/node
// js script that concats 2 files
const fs = require('fs');
const first = process.argv[2];
const second = process.argv[3];
const path = process.argv[4];
// read first
let alltext = fs.readFileSync(first,
  { encoding: 'utf8', flag: 'r' },
  function (err, data) {
    if (err) { console.log(err); }
  });
// add second
alltext += fs.readFileSync(second,
  { encoding: 'utf8', flag: 'r' },
  function (err, data) {
    if (err) { console.log(err); }
  });
// write to path
fs.writeFileSync(path, alltext);
