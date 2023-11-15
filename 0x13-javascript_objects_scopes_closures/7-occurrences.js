#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let elem = 0;
  for (i in list) {
    if (list[i] === searchElement) {
      elem += 1;
    }
  }
  return elem;
};
