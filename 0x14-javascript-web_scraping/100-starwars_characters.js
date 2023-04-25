#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
let def = {};
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const letter = JSON.parse(body);
    letter.characters.forEach(function (item, index, array) {
      request(item, function (error, response, data) {
        if (error) {
          console.log(error);
        } else {
          def = JSON.parse(data);
          console.log(def.name);
        }
      });
    });
  }
});
