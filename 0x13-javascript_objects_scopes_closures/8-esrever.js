#!/usr/bin/node

exports.esrever = function (list) {
  const rvList = [];
  for (let i = list.length - 1; i >= 0; i--) { rvList.push(list[i]); }
  return rvList;
};
