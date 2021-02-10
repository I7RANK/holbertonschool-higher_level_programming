#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');

fs.readFile(argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
