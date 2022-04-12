#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const jsonObj = JSON.parse(body).results;
    let count = 0;
    for (const film in jsonObj) {
      const characters = jsonObj[film].characters;
      for (const characterId in characters) {
        if (characters[characterId].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Error: ' + res.statusCode);
  }
}
);
