#!/usr/bin/node
const list = require('./100-data.js').list;

const mapList = list.map(function (value, index) {
  return value * index;
});

console.log(list);
console.log(mapList);
