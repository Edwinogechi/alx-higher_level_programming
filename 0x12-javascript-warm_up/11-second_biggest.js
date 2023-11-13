#!/usr/bin/node

// Check if the number of arguments passed via the command line is 3 or less
if (process.argv.length <= 3) {
  // In case of insufficient arguments, print 0
  console.log(0);
} else {
  // Convert the provided command-line arguments into an array of numbers,
  // then exclude the first two elements (executable and script names),
  // and finally, sort the numbers in ascending order
  const args = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);

  // Display the second-to-last (penultimate) number from the sorted array
  console.log(args[args.length - 2]);
}
