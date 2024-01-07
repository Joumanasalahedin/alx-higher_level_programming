#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2];

request(apiURL, function (err, res, body) {
  if (err == null) {
    let count = 0;
    const data = JSON.parse(body);
    data.results.forEach(film => {
      if (film.characters.some(characterUrl => characterUrl.endsWith('/18/'))) {
        count++;
      }
    });

    console.log(count);
  }
});
