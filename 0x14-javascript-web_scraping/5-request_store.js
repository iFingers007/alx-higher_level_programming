#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Error: Provide url and file path');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.log('Error writing to file:', err);
      }
    });
  } else {
    console.error('Failed to retrieve webpage:', error);
  }
});
