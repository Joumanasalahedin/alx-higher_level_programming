#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    fs.writeFileSync(file, body);
  }
});
