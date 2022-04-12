#!/usr/bin/node

const episode = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
const request = require('request');

request(url + episode, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const jsonObj = JSON.parse(body);
    console.log(jsonObj.title);
  } else {
    console.log('Error: ' + res.statusCode);
  }
}
);
