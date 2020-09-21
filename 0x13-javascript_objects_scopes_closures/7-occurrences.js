#!/usr/bin/node
// returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return count;
};
