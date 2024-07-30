#!/usr/bin/node

const request = require('request');

const filePath = process.argv[2];

if (!filePath) {
  console.error('Error: Provide file path');
  process.exit(1);
}

request(filePath, function(error, response, body) {
  console.error('error:', error);
  console.log('code:', response && response.statusCode);
});
