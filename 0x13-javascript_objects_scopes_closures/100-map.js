#!/usr/bin/node

const myarr = require('./100-data').list;

console.log(myarr);
console.log(myarr.map((x, idx) => x * idx));i
