#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request(url, (e, response, body) => {
  console.log(JSON.parse(body).title);
});
