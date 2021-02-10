#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

const url = argv[2];

const userTasks = {};

request(url, (e, response, body) => {
  const users = JSON.parse(body);

  for (let i = 0; i < users.length; i++) {
    if (users[i].completed === true) {
      if (userTasks[users[i].userId]) {
        userTasks[users[i].userId] += 1;
      } else {
        userTasks[users[i].userId] = 1;
      }
    }
  }

  console.log(userTasks);
});
