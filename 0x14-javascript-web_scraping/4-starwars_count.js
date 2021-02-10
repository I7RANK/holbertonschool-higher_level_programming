#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

const url = argv[2];

request(url, (e, response, body) => {
  const films = JSON.parse(body).results;
  let count = 0;

  for (let i = 0; i < films.length; i++) {
    const characters = films[i].characters;

    for (let j = 0; j < characters.length; j++) {
      if (characters[j].includes('/18')) {
        count++;
      }
    }
  }

  console.log(count);
});
