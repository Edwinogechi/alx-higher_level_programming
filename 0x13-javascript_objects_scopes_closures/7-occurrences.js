#!/usr/bin/node

// Export a function named nbOccurences
exports.nbOccurences = function (list, searchElement) {
  // Initialize a counter to keep track of occurrences
  let count = 0;

  // Use the map function to iterate over each element in the list
  list.map((x) => {
    // Check if the current element is equal to the searchElement
    if (x === searchElement) {
      // If true, increment the count
      count += 1;
      // Return 1 (not used, can be removed)
      return 1;
    } else {
      // If false, return 0 (not used, can be removed)
      return 0;
    }
  }
  );

  // Return the final count of occurrences
  return count;
};
