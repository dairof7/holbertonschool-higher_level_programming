#!/usr/bin/node
const { list } = require('./100-main');
const newlist = [];
list.map((element, index) => {
  newlist.push(element * index);
});
console.log(list);
console.log(newlist);
