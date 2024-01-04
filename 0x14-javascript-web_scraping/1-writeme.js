#!/usr/bin/node

// Import the 'fs' module for file system operations
const fs = require('fs');

// Retrieve the file path and data to write from the command-line arguments
const filePath = process.argv[2];
const writeData = process.argv[3];

// Write data to the specified file asynchronously
fs.writeFile(filePath, writeData, 'utf-8', (error) => {
  // Check if there is an error during file writing
  if (error) {
    console.log(error); // Log the error to the console
  } else {
    console.log(`Data written to ${filePath}`); // Log a success message
  }
});
