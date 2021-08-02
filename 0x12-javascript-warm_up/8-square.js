#!/usr/bin/node
let i, j;
let string = '';
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    for (j = 0; j < size; j++) {
      string = string + 'X';
    }
    console.log(string);
    string = '';
  }
}
