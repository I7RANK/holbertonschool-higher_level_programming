#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request(url, (e, response, body) => {
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; i++) {
    request(characters[i], (eChar, resChar, bodyChar) => {
      console.log(JSON.parse(bodyChar).name);
    });
  }
});
