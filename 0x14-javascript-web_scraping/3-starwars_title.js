#!/usr/bin/node
const argu = process.argv;
const num = argu[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + num;
const request = require('request');

request(url, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    const info = JSON.parse(body);
    console.log(info.title);
  }
});
