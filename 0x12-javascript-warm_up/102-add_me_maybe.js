#!/usr/bin/node
// js function thatt increments and calls a function
exports.addMeMaybe = function (number, theFunction) {
  number += 1;
  theFunction(number);
};
