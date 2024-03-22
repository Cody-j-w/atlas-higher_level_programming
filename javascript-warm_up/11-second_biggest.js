#!/usr/bin/node

const { argv } = require('node:process');

let max = 0;
let res = 0;

for (let i = 2; i < argv.length; i++) {
  const value = Number(argv[i]);
  if (isNaN(value)) {
    continue;
  } else if (value > max) {
    [res, max] = [max, value];
  } else if (value < max && value > res) {
    res = value;
  }
}

console.log(res);
