#!/usr/bin/node

const url = 'https://swapi-api.hbtn.io/api/films/';
const movie = process.argv[2];
const request = require('request');

request(url + movie, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const film = JSON.parse(body);
    for (const i in film.characters) {
      request(film.characters[i], function (err, res, body) {
        if (err) {
          console.log(err);
        } else if (res.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
      // console.log(film.characters[i]);
    }
  } else {
    console.log('Error: ' + res.statusCode);
  }
}
);
