#!/usr/bin/node
const { list } = require('./100-data');
const newlist = [];
list.map((element, index) => {
  newlist.push(element * index);
});
console.log(list);
console.log(newlist);
