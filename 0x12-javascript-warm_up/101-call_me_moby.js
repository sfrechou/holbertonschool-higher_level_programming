#!/usr/bin/node
// js file thatt executes x times a function
exports.callMeMoby = function (x, theFunction) {
  let i;
  for (i = 0; i < x; i++) {
    theFunction();
  }
};
