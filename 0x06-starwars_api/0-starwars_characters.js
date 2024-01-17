#!/usr/bin/node

// script that prints all characters of a Star Wars movie:

const request = require('request');
const movieId = process.argv[2];

function getMovieChars (movieId) {
// Make a request to the SWAPI films endpoint
  const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

  request(filmUrl, { json: true }, (err, res, body) => {
    if (err) {
      console.error(`Error fetching film data ${err.message}`);
      return;
    }

    console.log(body);

    const charUrls = body.characters;

    // Iterate through characters url and their names
    charUrls.forEach(charUrl => {
      request(charUrl, { json: true }, (charErr, charRes, charBody) => {
        if (charErr) {
          console.error(`Error fetching char data ${charErr.message}`);
          return;
        }

        console.log(charBody.name);
      });
    });
  });
}

// Check for movieId in command line argument

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

// Call the function to print the movie chars
getMovieChars(movieId);
