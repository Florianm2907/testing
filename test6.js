// // const fs = require('fs');

// function cipher_ii(input_bytes, key) {
//     let previousOutput = 0;
//     const output_bytes = [];

//     for (const byte of input_bytes) {
//         const current_key = previousOutput ^ key;
//         const xor_byte = byte ^ current_key;
//         previousOutput = xor_byte;
//         output_bytes.push(xor_byte);
//     }

//     return output_bytes;
// }

// // function cipher_i(encrypted_hex_string) {
// //     const key = 42;
// //     const encrypted_bytes = convert_hex_string_to_bytes(encrypted_hex_string);
// //     const decrypted_bytes = [];

// //     for (const byte of encrypted_bytes) {
// //         const original_byte = byte ^ key;
// //         decrypted_bytes.push(original_byte);
// //     }

// //     // Convert decrypted bytes back to string
// //     const decrypted_message = String.fromCharCode(...decrypted_bytes);

// //     return decrypted_message;
// // }
// function find_key_and_message(encrypted_bytes) {
//     let possibleMessages = [];
//     let possibleKeys = [];

//     for (let possibleKey = 0; possibleKey < 255; possibleKey++) {
//         const decrypted_bytes = cipher_ii(encrypted_bytes, possibleKey);
//         const decrypted_message = String.fromCharCode(...decrypted_bytes);

//         possibleMessages.push(decrypted_message);
//         possibleKeys.push(possibleKey);
//     }

//     return { possibleMessages, possibleKeys };
// }
// // function convert_hex_string_to_bytes(hex_string) {
// //     const bytes = [];
// //     for (let i = 0; i < hex_string.length; i += 2) {
// //         bytes.push(parseInt(hex_string.slice(i, i + 2), 16));
// //     }
// //     return bytes;
// // }


// // // Example usage:
// // const encrypted_hex_string = "6d5f5e4f0a6b58484f435e0b0a6e434f0a6b445e5d45585e0a464b5f5e4f5e0a6b6f7904";
// // const encrypted_bytes = convert_hex_string_to_bytes(encrypted_hex_string); // Define the convert_hex_string_to_bytes function
// // const textt = cipher_i(encrypted_bytes)
// // console.log(textt)
// // // const { possibleMessages, possibleKeys } = find_key_and_message(encrypted_bytes);
// // // const content = possibleMessages.join('\n');
// // // const filePath = 'output.txt';
// // // fs.writeFileSync(filePath, content, 'utf-8');

// // // console.log("Possible Keys:", possibleKeys);
// // // console.log("Possible Messages:", possibleMessages);


// function ascii_string_to_bytes(input_string) {
//     const bytes = [];
//     for (let i = 0; i < input_string.length; i++) {
//         bytes.push(input_string.charCodeAt(i));
//     }
//     return bytes;
// }

// function convert_bytes_to_hex_string(bytes) {
//     return bytes.map(byte => byte.toString(16).padStart(2, '0')).join('');
// }

// function convert_hex_string_to_bytes(hex_string) {
//     const bytes = [];
//     for (let i = 0; i < hex_string.length; i += 2) {
//         bytes.push(parseInt(hex_string.slice(i, i + 2), 16));
//     }
//     return bytes;
// }

// function cipher(input_string) {
//     const key = 42;
//     const input_bytes = ascii_string_to_bytes(input_string);
//     const output_bytes = [];

//     for (const byte of input_bytes) {
//         const xor_byte = byte ^ key;
//         output_bytes.push(xor_byte);
//     }

//     return convert_bytes_to_hex_string(output_bytes);
// }

// function decipher(encrypted_hex_string) {
//     const key = 42;
//     const encrypted_bytes = convert_hex_string_to_bytes(encrypted_hex_string);
//     const decrypted_bytes = [];

//     for (const byte of encrypted_bytes) {
//         const original_byte = byte ^ key;
//         decrypted_bytes.push(original_byte);
//     }

//     // Convert decrypted bytes back to string
//     const decrypted_message = String.fromCharCode(...decrypted_bytes);

//     return decrypted_message;
// }

// // Example usage:
// const message = "string";
// const encrypted_hex_string = "4c2f513f5a3256355d3e577a1e60193458204e2b066f0b631d750a27690d70157d022f4c2846235a771b740a68097108255b3f51345c23002d680c641b365f3753305875395a23593b443d0a27781c6206600221";
// console.log("Encrypted: " + encrypted_hex_string);

// const decrypted_message = decipher(encrypted_hex_string);
// console.log("Decrypted: " + decrypted_message);
// for(i = 0; i < 255; i++){
//     console.log(cipher_ii(convert_hex_string_to_bytes(encrypted_hex_string), i))
// }