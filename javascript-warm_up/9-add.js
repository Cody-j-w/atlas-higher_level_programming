#!/usr/bin/node

const { argv } = require('node:process');

arg1 = Number(argv[2]);
arg2 = Number(argv[3]);


console.log(parseInt(+arg1 + +arg2));
