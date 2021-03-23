#!/usr/bin/node
// js script that imports an array and computes a new array
const list = require('./100-data').list;

const newArr = list.map((currElement, index) => currElement * index);

console.log(list);
console.log(newArr);
