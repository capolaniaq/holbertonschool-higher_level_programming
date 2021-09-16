#!/usr/bin/node

const request = require('request');
const finaldict = {};
let user = 1;
let taskdone = 0;

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    tasks.forEach(element => {
      if (element.userId !== user) {
        finaldict[user] = taskdone;
        taskdone = 0;
        user = element.userId;
      }
      if (element.completed === true) {
        taskdone += 1;
      }
    });
    finaldict[user] = taskdone;
    console.log(finaldict);
  }
});
