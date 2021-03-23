#!/usr/bin/node
// js function that converts a number from base 10 to another base passed as argument
exports.converter = function (base) {
  function number (num) {
    return (num.toString(base));
  }
  return number;
};
