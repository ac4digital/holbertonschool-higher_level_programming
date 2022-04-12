#!/usr/bin/node

const fs = require('fs');
const file_name = process.argv[2];
const text_file = process.argv[3];

fs.writeFile(file_name, text_file, 'utf-8', function (err, data) {
	if (err) {
		console.log(err);
	}
}
);
