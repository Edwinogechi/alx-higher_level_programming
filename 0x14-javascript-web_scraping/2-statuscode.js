#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Retrieve the URL from the command-line arguments
const url = process.argv[2];

// Perform an HTTP GET request to the specified URL using the 'request' module
request
  .get(url)
  // Set up an event listener for the 'response' event emitted by the HTTP request
  .on('response', (response) => {
    // Log the HTTP status code of the response to the console
    console.log('Status Code: ' + response.statusCode);
  });
