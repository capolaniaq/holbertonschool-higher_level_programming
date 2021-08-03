#!/usr/bin/node
let args = process.argv.slice(2);
args = args.sort();
console.log(args[args.length - 2]);
