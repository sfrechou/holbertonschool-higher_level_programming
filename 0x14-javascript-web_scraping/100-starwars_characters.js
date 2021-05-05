#!/usr/bin/node
const argu = process.argv;
const movieId = argu[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const chars = JSON.parse(body).characters;
    for (let i = 0; i < chars.length; i++) {
      request(chars[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const char = JSON.parse(body);
          console.log(char.name);
        }
      });
    }
  }
});
