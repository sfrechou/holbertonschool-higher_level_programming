#!/usr/bin/node
// js script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence
const dict = require('./101-data').dict;
const invertKeyValues = (dict, fn) =>
  Object.keys(dict).reduce((acc, key) => {
    const val = fn ? fn(dict[key]) : dict[key];
    acc[val] = acc[val] || [];
    acc[val].push(key);
    return acc;
  }, {});
console.log(invertKeyValues(dict));
