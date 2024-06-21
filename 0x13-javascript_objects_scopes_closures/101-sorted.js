#!/usr/bin/node
// Import the dictionary from data.js
const dict = require('./data.js').dict;

const result = {};

for (const [userId, occurrence] of Object.entries(dict)) {
  if (!result[occurrence]) {
    result[occurrence] = [];
  }
  result[occurrence].push(userId);
}

console.log(result);
