#!/usr/bin/node
// imports a dictionary of occurrences by user
// id and computes a dictionary of user ids by occurrence

const { dict } = require('./101-data');
const newdict = {};
for (const key in dict) {
  if (dict[key] in newdict) {
    newdict[dict[key]].push(key);
  } else {
    newdict[dict[key]] = [key];
  }
}
console.log(newdict);
