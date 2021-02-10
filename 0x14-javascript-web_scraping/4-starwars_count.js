#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/people/18';

request(url, (e, response, body) => {
  console.log(JSON.parse(body).films.length);
});
