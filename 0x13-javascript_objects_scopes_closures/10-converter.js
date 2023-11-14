#!/usr/bin/node
exports.converter = function (base) {
  return function (j) {
    return j.toString(base);
  };
};
