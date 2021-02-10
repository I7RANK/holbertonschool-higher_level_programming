#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request(argv[2], (any, response) => {
  console.log('code:', response.statusCode);
});
