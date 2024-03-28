#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');
let count = 0;
request(argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    for (const film of data.results) {
      for (const character of film.characters) {
        if (character === 'https://swapi-api.hbtn.io/api/people/18/') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
