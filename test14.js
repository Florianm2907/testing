const fs = require('fs');
const crypto = require('crypto');

const salt = '3NL/usjb4vEg';
const hash = '47fde76c898053a9db963df844bb936c26ab54867663f4d1505858d6c346eacc';

// Function to hash a password with the given salt using SHA256
function hashPassword(password) {
  return crypto.createHash('sha256').update(salt + password).digest('hex');
}

// Function to read passwords from a file and compare their hashes with the given hash
function checkPasswordsFromFile(filePath) {
  try {
    const passwords = fs.readFileSync(filePath, 'utf-8').split('\n');

    for (const password of passwords) {
      const hashedPassword = hashPassword(password.trim());

      if (hashedPassword === hash) {
        console.log(`Password found: ${password}`);
        return true; // You can return the password or perform further actions if needed
      }
    }

    console.log('No matching password found.');
    return false;
  } catch (error) {
    console.error(`Error reading file: ${error.message}`);
    return false;
  }
}

// Example usage
const filePath = 'F:/FESTPLATTE H/test1/max.txt';
checkPasswordsFromFile(filePath);
