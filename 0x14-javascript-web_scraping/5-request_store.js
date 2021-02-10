#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');
const request = require('request');

const url = argv[2];

request(url, (e, response, body) => {
  fs.writeFile(argv[3], body, { flag: 'w+' }, err => {
    if (err) {
      console.error(err);
    }
  });
});
