#!/usr/bin/node
const argu = process.argv;
const url = argu[2];
const https = require('https');
const request = https.get(url, function (response) {
  console.log('code: ' + response.statusCode);
});

request.on('error', function (error) {
  console.error('code: ' + error.status);
});
