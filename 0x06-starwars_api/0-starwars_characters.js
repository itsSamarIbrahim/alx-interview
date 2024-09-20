#!/usr/bin/env node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID.');
  process.exit(1);
}

const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

function fetchCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }

      if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch character data. Status Code: ${response.statusCode}`));
        return;
      }

      resolve(body.name);
    });
  });
}

request(movieUrl, { json: true }, async (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data. Status Code: ${response.statusCode}`);
    process.exit(1);
  }

  const characters = body.characters;
  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  try {
    for (const characterUrl of characters) {
      const name = await fetchCharacterName(characterUrl);
      console.log(name);
    }
  } catch (err) {
    console.error('Error:', err);
  }
});
