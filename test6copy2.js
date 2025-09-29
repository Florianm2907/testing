// // // Define the provided functions
// // function ascii_string_to_bytes(input_string) {
// //     const bytes = [];
// //     for (let i = 0; i < input_string.length; i++) {
// //         bytes.push(input_string.charCodeAt(i));
// //     }
// //     return bytes;
// // }

// // function convert_bytes_to_hex_string(bytes) {
// //     return bytes.map(byte => byte.toString(16).padStart(2, '0')).join('');
// // }

// // // Define the cipher_ii function
// // function cipher_ii(input_bytes, key) {
// //     let previousOutput = 0;
// //     const output_bytes = [];

// //     for (const byte of input_bytes) {
// //         const current_key = previousOutput ^ key;
// //         const xor_byte = byte ^ current_key;
// //         previousOutput = xor_byte;
// //         output_bytes.push(xor_byte);
// //     }

// //     return output_bytes;
// // }

// // function convert_hex_string_to_bytes(hex_string) {
// //     const bytes = [];

// //     for (let i = 0; i < hex_string.length; i += 2) {
// //         bytes.push(parseInt(hex_string.substr(i, 2), 16));
// //     }

// //     return bytes;
// // }


// // // Provided ciphered output
// // const cipheredHex = "4c2f513f5a3256355d3e577a1e60193458204e2b066f0b631d750a27690d70157d022f4c2846235a771b740a68097108255b3f51345c23002d680c641b365f3753305875395a23593b443d0a27781c6206600221";

// // // Convert cipheredHex to bytes
// // const cipheredBytes = convert_hex_string_to_bytes(cipheredHex); // You need to define this function

// // // Try all possible keys and decrypt
// // for (let key = 0; key <= 256; key++) {
// //     const decryptedBytes = cipher_ii(cipheredBytes, key);
// //     const decryptedMessage = String.fromCharCode(...decryptedBytes);
    
// //     console.log(decryptedMessage.toString());
// // }


// // Define the provided functions
// function convert_bytes_to_hex_string(bytes) {
//     return bytes.map(byte => byte.toString(16).padStart(2, '0')).join('');
// }

// function convert_hex_string_to_bytes(hex_string) {
//     const bytes = [];

//     for (let i = 0; i < hex_string.length; i += 2) {
//         bytes.push(parseInt(hex_string.substr(i, 2), 16));
//     }

//     return new Uint8Array(bytes);
// }

// // Define the cipher_ii function
// function cipher_ii(input_bytes, key) {
//     let previousOutput = 0;
//     const output_bytes = new Uint8Array(input_bytes.length);

//     for (let i = 0; i < input_bytes.length; i++) {
//         const byte = input_bytes[i];
//         const current_key = previousOutput ^ key;
//         const xor_byte = byte ^ current_key;
//         previousOutput = xor_byte;
//         output_bytes[i] = xor_byte;
//     }

//     return output_bytes;
// }

// // Provided ciphered output
// const cipheredHex = "4c2f513f5a3256355d3e577a1e60193458204e2b066f0b631d750a27690d70157d022f4c2846235a771b740a68097108255b3f51345c23002d680c641b365f3753305875395a23593b443d0a27781c6206600221";

// // Convert cipheredHex to bytes
// const cipheredBytes = convert_hex_string_to_bytes(cipheredHex);

// // Try all possible keys and decrypt
// // for (let key = 42; key <= 42; key++) {
// //     const decryptedBytes = cipher_ii(cipheredBytes, key);
    
// //     // Decode the bytes as UTF-8
// //     const decoder = new TextDecoder('utf-8');
// //     const decryptedMessage = decoder.decode(decryptedBytes);
    
// //     console.log(decryptedMessage);
// // }
// messages = []
// for (let key = 0; key <= 255; key++) {
//     const decryptedBytes = cipher_ii(cipheredBytes, key);
//     const decryptedMessage = String.fromCharCode(...decryptedBytes);
//     messages.push(decryptedMessage)
//     console.log(`Key ${key}: ${decryptedMessage}`);
// }
// const searchString = ' ';

// const found = messages.some(item => item.includes(searchString));

// if (found) {
//     console.log(`String '${searchString}' found in the array.`);
// } else {
//     console.log(`String '${searchString}' not found in the array.`);
// }

function cipher(input_bytes, key) {
    let previousOutput = 0;
    const output_bytes = [];

    for (const byte of input_bytes) {
        const current_key = previousOutput ^ key;
        const xor_byte = byte ^ current_key;
        previousOutput = xor_byte;
        output_bytes.push(xor_byte);
    }

    return output_bytes;
}

function decipher(input_bytes, key) {
    let previousOutput = 0;
    const output_bytes = [];

    for (const byte of input_bytes) {
        const current_key = previousOutput ^ key;
        const xor_byte = byte ^ current_key;
        previousOutput = byte; // Set previousOutput for the next iteration
        output_bytes.push(xor_byte);
    }

    // Convert decrypted bytes to UTF-8 text
    const textDecoder = new TextDecoder('utf-8');
    const decrypted_message = textDecoder.decode(new Uint8Array(output_bytes));

    return decrypted_message;
}

// Example usage:
const message = "Hello, World!";
const key = 42;

// Encryption
const bytes = new TextEncoder().encode(message);
const encrypted_bytes = "6d5f5e4f0a6b58484f435e0b0a6e434f0a6b445e5d45585e0a464b5f5e4f5e0a6b6f7904"

// Decryption
const decrypted_message = decipher(encrypted_bytes, key);
console.log("Original Message: " + message);
console.log("Encrypted Bytes: " + encrypted_bytes);
console.log("Decrypted Message: " + decrypted_message);

function tryAllKeys(encrypted_hex_string) {
    for (let key = 0; key < 256; key++) {
        setTimeout(() => {
            console.clear();
            let decrypted_message = decipher(encrypted_hex_string, key);
            console.log("Key: " + key + ", Decrypted: " + decrypted_message);
        }, key * 500); // Delay output by key * 500 milliseconds (0.5 seconds)
    }
}

// Example usage:
// const encrypted_hex_string = "4c2f513f5a3256355d3e577a1e60193458204e2b066f0b631d750a27690d70157d022f4c2846235a771b740a68097108255b3f51345c23002d680c641b365f3753305875395a23593b443d0a27781c6206600221"; // Replace with the actual encrypted hex string
// // tryAllKeys(encrypted_hex_string);
// console.log(decipher("6d5f5e4f0a6b58484f435e0b0a6e434f0a6b445e5d45585e0a464b5f5e4f5e0a6b6f7904", 42))