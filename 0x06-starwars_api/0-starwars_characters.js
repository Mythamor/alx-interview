#!/usr/bin/node

// script that prints all characters of a Star Wars movie:

const request = require('request');

const movieId = process.argv[2];
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// Recursive function that iterates over charUrls
// It makes assynchronous requests for each url and logs char names to console
function sendRequest (charList, index) {
// Make a request to the SWAPI films endpoint
  if (index === charList.length) {
    return;
  }

  request(charList[index], { json: true }, (err, res, body) => {
    if (err) {
      console.error(`Error fetching char data ${err.message}`);
    } else {
      console.log(body.name);
    }

    sendRequest(charList, index + 1);
  });
}

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

// Asynch requests to extract list of char urls
request(filmUrl, { json: true }, (err, res, body) => {
  if (err) {
    console.error(`Error fetching char data ${err.message}`);
  } else {
    const charList = body.characters;
    sendRequest(charList, 0);
  }
});
