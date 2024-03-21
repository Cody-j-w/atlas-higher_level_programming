#!/usr/bin/node

const { argv } = require('node:process');

let flag = 'too short';
argv.forEach((val, index) => {
  if (index === 2) {
    flag = 'argument provided';
    console.log(val);
  }
});
if (flag === 'too short') {
  console.log('No argument');
}
