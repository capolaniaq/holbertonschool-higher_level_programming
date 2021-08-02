#!/usr/bin/node
function factorial (number) {
  const mynumber = parseInt(number);
  if (isNaN(mynumber)) {
    return 1;
  }
  if (mynumber === 0) {
    return 1;
  }
  return mynumber * factorial(mynumber - 1);
}
const fact = factorial(process.argv[2]);
console.log(fact);
