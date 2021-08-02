#!/usr/bin/node
const mynumber = parseInt(process.argv[2]);
if (isNaN(mynumber)) {
  console.log('Not a number');
} else {
  console.log('my number: ' + mynumber);
}
