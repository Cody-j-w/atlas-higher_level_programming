#!/usr/bin/node

const { argv, env } = require('node:process');
const request = require(`${env.NODE_PATH}/request`);

request(argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
