#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

if (!filePath || !contentToWrite) {
  console.error('Error: Provie file path and string');
  process.exit(1);
}

// Step 2: Read the file content using 'fs.readFile'
fs.writeFile(filePath, contentToWrite, 'utf8', (err) => {
  if (err) {
    // Handle errors that occur during file reading
    console.error(err);
    return;
  }
  console.log('Writing to file completed');
});
