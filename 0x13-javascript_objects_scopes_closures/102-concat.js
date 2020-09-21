#!/usr/bin/node
const { promises: fs } = require('fs');

async function f1 (path) {
  return fs.readFile(path, 'utf-8');
}

(async () => {
  const content = await f1(process.argv[2]);
  const content2 = await f1(process.argv[3]);
  fs.writeFile(process.argv[4], content + '\n' + content2);
})();
