#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const jsonObj = JSON.parse(body);
    const completed = {};
    for (const i in jsonObj) {
      const task = jsonObj[i];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('Error: ' + res.statusCode);
  }
}
);
