#!/usr/bin/node
const fetch = require('node-fetch');
const filmID = process.argv[2];

if (!filmID) {
  console.error('Usage: ./fetch_characters.js <Film ID>');
  process.exit(1);
}

async function fetchCharacters (filmId) {
  const endpoint = `https://swapi.dev/api/films/${filmId}`;
  try {
    const response = await fetch(endpoint);
    if (!response.ok) {
      throw new Error(`Failed to fetch film: ${response.status}`);
    }
    const data = await response.json();


    for (const url of data.characters) {
      const charResponse = await fetch(url);
      if (!charResponse.ok) {
        throw new Error(`Failed to fetch character: ${charResponse.status}`);
      }
      const charData = await charResponse.json();
      console.log(charData.name);
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

fetchCharacters(filmID);
