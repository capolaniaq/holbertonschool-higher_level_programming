#!/usr/bin/node
let i;
if (process.argv[2]) {
  if (process.argv[2] > 0) {
    for (i = 0; i < process.argv[2]; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
