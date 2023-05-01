#!/usr/bin/node

const args = process.argv[1];
const request = require('request');
request(args, function (body, error) {
  console.log(body);
  console.log(error);
});
