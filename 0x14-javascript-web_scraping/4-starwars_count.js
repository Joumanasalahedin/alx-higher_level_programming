#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2]; // Get the API URL from command line argument


request(apiURL, { json: true }, (err, res, body) => {
    const wedgeAntillesId = 18;
    let count = 0;

    body.results.forEach(film => {
        if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
            count++;
        }
    });

    console.log(count);
});

