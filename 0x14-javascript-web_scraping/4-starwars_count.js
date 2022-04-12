#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, res, body) {
    if (err) {
        console.log(err);
    } else if (res.statusCode === 200) {
        let json_obj = JSON.parse(body).results;
        let count = 0;
        for (let film in json_obj) {
            let characters = json_obj[film].characters;
            for (let character_id in characters) {
                if (characters[character_id].includes('18')) {
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
