#!/usr/bin/node
const argu = process.argv;
const fs = require('fs');
fs.writeFile(argu[2], argu[3], function (err) {
  if (err) {
    return console.log(err);
  }
});
