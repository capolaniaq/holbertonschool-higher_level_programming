#!/usr/bin/node

const fs = require('fs');

fs.writeFileSync(process.argv[2], process.argv[3], 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});