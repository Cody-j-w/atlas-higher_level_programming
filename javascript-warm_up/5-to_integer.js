#!/usr/bin/node

const { argv } = require('node:process');

let argument = argv[2];

if (isNaN(Number(argument))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Math.floor(Number(argument)));
}
