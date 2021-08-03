#!/usr/bin/node
let args = process.argv.slice(2);
args = args.sort(function (a, b) { return a - b; });
console.log(args[args.length - 2]);
