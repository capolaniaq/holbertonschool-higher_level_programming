#!/usr/bin/node

const request = require('request');
let number = '';
let characters = [];
let id = '';

if (process.argv[2]) {
  let count = 0;
  for (let i = 1; i < 8; i++) {
    number = i.toString();
    number = process.argv[2] + '/' + number;
    request.get(number, function (error, response, body) {
      if (error) {
        console.log(error);
      } else {
        characters = JSON.parse(body).characters;
        let j = 0;
        while (j < characters.length) {
          if (characters[j] !== undefined) {
            id = characters[j].substr(-3);
          }
          if (id === '18/') {
            count += 1;
          }
          j++;
        }
        if (i === 7) {
          console.log(count);
        }
      }
    });
  }
}
