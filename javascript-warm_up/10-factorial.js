#!/usr/bin/node

const { argv } = require('node:process');

function factorial (int) {
  if (Number(int) === 1 || Number(int) === 0 || isNaN(Number(int))) {
    return 1;
  } else {
    return (int * factorial(int - 1));
  }
}

console.log(factorial(argv[2]));
