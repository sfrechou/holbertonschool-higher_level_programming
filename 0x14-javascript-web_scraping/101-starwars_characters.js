#!/usr/bin/node
const argu = process.argv;
const movieId = argu[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
const request = require('request');

function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, response, body) {
      if (error) {
        reject(console.log(error));
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

// Usage:

async function main (chars) {
  for (let j = 0; j < chars.length; j++) {
    const res = await doRequest(chars[j]);
    console.log(res);
  }
}

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const chars = JSON.parse(body).characters;
    main(chars);
  }
});
