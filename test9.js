// const fs = require('fs');

// const salt = '3NL/usjb4vEg'
// const hash = '47fde76c898053a9db963df844bb936c26ab54867663f4d1505858d6c346eacc'

// const value = "?"
// if (sha256(salt + value).hex() !== hash) {
//     alert('Passwort falsch.')
//     return false
// }

const fs = require('fs');
const crypto = require('crypto');

const salt = '3NL/usjb4vEg';
const hash = '47fde76c898053a9db963df844bb936c26ab54867663f4d1505858d6c346eacc';

// Read the text file line by line
const filename = 'C:/Users/Florian/Downloads/cupp-master/cupp-master/max.txt'; // Replace with your text file path

const data = fs.readFileSync(filename, 'utf-8');
const lines = data.split('\n');

for (const line of lines) {
  const value = line.trim(); // Assuming each line is a value to hash
  const calculatedHash = crypto.createHash('sha256').update(salt + value).digest('hex');

  if (calculatedHash === hash) {
    console.log(`Match found: ${value}`);
    break; // Stop searching after the first match
  }
}
