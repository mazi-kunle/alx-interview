#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const baseUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(baseUrl, function (err, res, body) {
  if (err) {
    console.log('An error occured');
  }
  const characters = JSON.parse(body).characters;
  if (characters && characters.length > 0) {
    getReq(0, characters, characters.length);
  }
});

function getReq (index, urls, length) {
  if (index === length) {
    return;
  }
  request(urls[index], function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      index++;
      getReq(index, urls, length);
    } else {
      console.log('error');
    }
  });
}
