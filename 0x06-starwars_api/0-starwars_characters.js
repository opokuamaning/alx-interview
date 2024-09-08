#!/usr/bin/node

const request = require("request");

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/${movieId}`;

request(url, (error, response, body) => {
    if (error) {
        console.log(error);
        return;
    }

    const filmData = JSON.parse(body);

    const characters = filmData.characters;
    characters.forEach((character) => {
        request(character, (error, response, body) => {
            if (error) {
                console.log(error);
                return;
            }

            const characterData = JSON.parse(body);
            console.log(characterData.name);
        });
    });
});