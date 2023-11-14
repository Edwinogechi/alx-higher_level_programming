#!/usr/bin/node
const dict = require('./101-data.js');

const newDict = {};
const inputs = dict.dict;

for (const key in inputs) {
  if (newDict[inputs[key]] === undefined) {
    newDict[inputs[key]] = [key];
  } else {
    newDict[inputs[key]].push(key);
  }
}

console.log(newDict);
