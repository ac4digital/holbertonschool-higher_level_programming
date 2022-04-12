#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];
const textFile = process.argv[3];

fs.writeFile(fileName, textFile, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
}
);
