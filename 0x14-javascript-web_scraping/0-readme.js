#!/usr/bin/node
const argu = process.argv;
const fs = require('fs');
fs.readFile(argu[2], 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
