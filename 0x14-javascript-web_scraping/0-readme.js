#!/usr/bin/node

// Import the 'fs' module for file system operations
const fs = require('fs');

// Retrieve the file path from the command-line arguments
const filePath = process.argv[2];

// Read the contents of the file asynchronously
fs.readFile(filePath, 'utf-8', (error, data) => {
  // Check if there is an error during file reading
  if (error) {
    console.log(error); // Log the error to the console
  } else {
    console.log(data); // Log the content of the file to the console
  }
});
