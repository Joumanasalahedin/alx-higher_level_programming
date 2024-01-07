#!/usr/bin/node
const request = require('request');
const movieid = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieid}`

request(url, function (error, response, body) {
    if (error == null) {
        const json = JSON.parse(body);
        console.log(json.title)
    }
})
