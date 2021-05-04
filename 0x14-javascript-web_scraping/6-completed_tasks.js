#!/usr/bin/node
const argu = process.argv;
const url = argu[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body);
    const dict = {};
    let currentId = results[0].userId;
    let done = 0;
    for (let i = 0; i < results.length; i++) {
      if (currentId === results[i].userId) {
        if (results[i].completed === true) {
          done++;
        }
      } else {
        if (done !== 0 && i > 0) {
          dict[results[i - 1].userId] = done;
          done = 0;
          currentId = results[i].userId;
          i--;
        }
      }
    }
    dict[results[results.length - 1].userId] = done;
    console.log(dict);
  }
}
);
