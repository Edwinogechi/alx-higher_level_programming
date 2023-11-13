#!/usr/bin/node

const n = parseInt(process.argv[2]);

function findFactorial (n) {
  if (!n) { return 1; }

  if (n <= 0) { return; }
  return findFactorial(n - 1) * n;
}

console.log(findFactorial(n));
