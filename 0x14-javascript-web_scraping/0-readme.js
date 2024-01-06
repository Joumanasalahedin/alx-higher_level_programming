#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2]
fs.readFile(file, 'utf-8', (err, body) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(body);
})
