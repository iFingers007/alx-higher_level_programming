#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

if (!filePath) {
  console.error('Error: No file path provided');
  process.exit(1);
}

// Step 2: Read the file content using 'fs.readFile'
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    // Handle errors that occur during file reading
    console.error(err);
    return;
  }

  // Print the file content if no error occurs
  console.log(data);
});
