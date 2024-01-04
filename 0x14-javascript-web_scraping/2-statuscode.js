#!/usr/bin/node

const request = require('request');
// Import the 'request' module for making HTTP requests.

request.get(process.argv[2])
// Initiate an HTTP GET request to the specified URL using the 'request' module.

  .on('response', function (response) {
    // Set up an event listener for the 'response' event emitted by the HTTP request.

    console.log(`Status Code: ${response.statusCode}`);
    // Log the HTTP status code of the response to the console.
  });
