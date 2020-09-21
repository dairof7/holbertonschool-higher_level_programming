#!/usr/bin/node
// returns the reversed version of a list:

exports.esrever = function (list) {
  const newlist = [];
  for (const i in list) {
    newlist.push(list[list.length - i - 1]);
  }
  return newlist;
};
