#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Retrieve the URL from the command-line arguments
const url = process.argv[2];

// Check if a URL is provided as a command-line argument
if (!url) {
  console.error('Usage: node 2-statuscode.js <URL>');
  process.exit(1); // Exit the process with an error code if no URL is provided
}

// Make an HTTP request to the specified URL using the 'request' module
request(url, (error, response) => {
  // Check for errors during the HTTP request
  if (error) {
    console.error(error); // Log the error to the console
  } else {
    // Log the HTTP status code of the response to the console
    console.log(`Status Code: ${response.statusCode}`);
  }
});
