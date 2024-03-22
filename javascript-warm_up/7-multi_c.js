#!/usr/bin/node

const { argv } = require('node:process');

for (let i = 0; i < argv[2]; i++) {
  console.log('C is fun');
}
