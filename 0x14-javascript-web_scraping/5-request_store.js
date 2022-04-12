#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(fileName, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
}
);
