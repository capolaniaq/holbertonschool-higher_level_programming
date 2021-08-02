#!/usr/bin/node
function add (a, b) {
  const number1 = parseInt(a);
  const number2 = parseInt(b);
  let sum = 0;
  if (isNaN(number1) || isNaN(number2)) {
    console.log('NaN');
  } else {
    sum = number1 + number2;
    console.log(sum);
  }
}
add(process.argv[2], process.argv[3]);
