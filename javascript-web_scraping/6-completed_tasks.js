#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const API = argv[2];
const todosList = {};
const usersList = [];
request(API, (err, res, body) => {
  if (err) {
    throw err;
  }
  const data = JSON.parse(body);
  for (const task of data) {
    if (!(usersList.includes(task.userId))) {
      usersList.push(task.userId);
    }
  }
  for (const id of usersList) {
    let count = 0;
    for (const task of data) {
      if (task.userId === id && task.completed === true) {
        count++;
      }
    }
    if (count !== 0) {
      todosList[id] = count;
    }
  }
  console.log(todosList);
});
