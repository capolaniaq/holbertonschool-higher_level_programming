#!/usr/bin/node

const fs = require('fs').promises;
const file = process.argv[2];

async function readFile (filePath) {
  try {
    const data = await fs.readFile(filePath);
    console.log(data.toString());
  } catch (error) {
    console.log({ error });
  }
}

readFile(file);
