const crypto = require('crypto');
const fs = require('fs');
const readline = require('readline');

const salt = '3NL/usjb4vEg';
const givenHash = '9bcf0c8289a97d33021b4790659396d9f8af1085210d2186b8ec38efcdc31472';

function calculateHash(word) {
  const hash = crypto.createHash('sha256');
  hash.update(salt + word);
  return hash.digest('hex');
}

function compareHashes(wordList, givenHash) {
  for (const word of wordList) {
    const wordHash = calculateHash(word);
    if (wordHash === givenHash) {
      console.log(`Found match: ${word}`);
      return;
    }
  }
  console.log('No match found.');
}

const wordList = []; // Store words from the text file

// Read words from a text file (one word per line)
const fileStream = fs.createReadStream('C:/Users/Florian/Downloads/cupp-master/cupp-master/max.txt');
const rl = readline.createInterface({
  input: fileStream,
  crlfDelay: Infinity
});

rl.on('line', (line) => {
  wordList.push(line);
});

rl.on('close', () => {
  compareHashes(wordList, givenHash);
});
