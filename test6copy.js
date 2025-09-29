function ascii_string_to_bytes(input_string) {
    const bytes = [];
    for (let i = 0; i < input_string.length; i++) {
        bytes.push(input_string.charCodeAt(i));
    }
    return bytes;
}

function convert_bytes_to_hex_string(bytes) {
    return bytes.map(byte => byte.toString(16).padStart(2, '0')).join('');
}

function convert_hex_string_to_bytes(hex_string) {
    const bytes = [];
    for (let i = 0; i < hex_string.length; i += 2) {
        bytes.push(parseInt(hex_string.substr(i, 2), 16));
    }
    return bytes;
}

function cipher(input_string) {
    const key = 42;
    const input_bytes = ascii_string_to_bytes(input_string);
    const output_bytes = [];

    for (const byte of input_bytes) {
        const xor_byte = byte ^ key;
        output_bytes.push(xor_byte);
    }

    return convert_bytes_to_hex_string(output_bytes);
}

// function decipher(encrypted_hex_string, key1, key2) {
//     let output_bytes = []
//     let encrypted_bytes = convert_hex_string_to_bytes(encrypted_hex_string);
//     let decrypted_bytes = [];
//     let previousOutput = 0
//     for (let i = 0; i < encrypted_bytes.length; i++) {
//         let current_key = previousOutput ^ (i % 2 === 0 ? key1 : key2);
//         let xor_byte = encrypted_bytes[i] ^ current_key;
//         previousOutput = xor_byte;
//         output_bytes.push(xor_byte);
//     }

//     // Convert decrypted bytes back to string
//     let textDecoder = new TextDecoder('utf-8');
//     let decrypted_message = textDecoder.decode(new Uint8Array(decrypted_bytes));

//     return decrypted_message;
// }


// encrypted_hex_string = "59176f2b4e4f377f1a5f7427431631306d294b066e2749062d7f1d523d3c55187226010051056d27491a317901547f2dda2403027c335c5d3f7d1e1f73375e1a31710f486d6c236b05044e017e284c1f60610646386d03567d1c2925030f3a36101c2925030f"
// for (let j = 1; j < 255; j++){
//     setTimeout((j) => {
//         // console.clear()
//         let decrypted_message = decipher(encrypted_hex_string, j, 1);
//         console.log("Key1: " + j + ", Key2: " + 0 + ", Decrypted: " + decrypted_message);
//     }, j * 500, j);
// }

function decipher_iii(encrypted_hex_string, key1, key2) {
    let encrypted_bytes = convert_hex_string_to_bytes(encrypted_hex_string);
    let previousOutput = 0;
    let output_bytes = [];

    for (let i = 0; i < encrypted_bytes.length; i++) {
        let current_key = previousOutput ^ (i % 2 === 0 ? key1 : key2);
        let xor_byte = encrypted_bytes[i] ^ current_key;
        previousOutput = encrypted_bytes[i];
        output_bytes.push(xor_byte);
    }

    // Convert decrypted bytes to UTF-8 text
    const textDecoder = new TextDecoder('ascii');
    const potential_decrypted_message = textDecoder.decode(new Uint8Array(output_bytes));
    return potential_decrypted_message;

}



// Example usage:
const encrypted_hex_string = "59176f2b4e4f377f1a5f7427431631306d294b066e2749062d7f1d523d3c55187226010051056d27491a317901547f2dda2403027c335c5d3f7d1e1f73375e1a31710f486d6c236b05044e017e284c1f60610646386d03567d1c2925030f3a36101c2925030f"; // Replace with the actual encrypted hex string
// console.log
let asd = []
for (let key1 = 0; key1 < 256; key1++){
    for (let key2 = 0; key2 < 256; key2++){
        asd.push("Key1: " + key1 + ", Key2: " + key2 + ", Ergebnis: " + decipher_iii(encrypted_hex_string, key1, key2))
        console.log("Key1: " + key1 + ", Key2: " + key2 + ", Decrypted: " + decipher_iii(encrypted_hex_string, key1, key2));
    }
}
for (let element of asd){
    if (element.includes("Antwort")){
        console.log(element)
    }
}
// console.log(cipher("6d5f5e4f0a6b58484f435e0b0a6e434f0a6b445e5d45585e0a464b5f5e4f5e0a6b6f7904"))


// function cipher(input_bytes) {
//     const key = 42;
//     const output_bytes = [];

//     for (const byte of input_bytes) {
//         const xor_byte = byte ^ key;
//         output_bytes.push(xor_byte);
//     }

//     return output_bytes;
// }

function decipher(encrypted_bytes) {
    const key = 42;
    let encrypted_bytes = convert_hex_string_to_bytes(encrypted_hex_string);
    const decrypted_bytes = [];

    for (const byte of encrypted_bytes) {
        const original_byte = byte ^ key;
        decrypted_bytes.push(original_byte);
    }

    return decrypted_bytes;
}
console.log(decipher(convert_hex_string_to_bytes("6d5f5e4f0a6b58484f435e0b0a6e434f0a6b445e5d45585e0a464b5f5e4f5e0a6b6f7904")))

// // Example usage:
// const message = "6d5f5e4f0a6b58484f435e0b0a6e434f0a6b445e5d45585e0a464b5f5e4f5e0a6b6f7904";
// const bytes = ascii_string_to_bytes(message); // You need to define the function ascii_string_to_bytes
// // const encrypted_bytes = cipher(bytes);
// const decrypted_bytes = decipher(message);

// // Convert decrypted bytes back to string
// // const decrypted_message = String.fromCharCode(...decrypted_bytes);

// console.log(convert_bytes_to_hex_string(decrypted_bytes));



// function cipher(input_bytes) {
//     const key = 42;
//     const output_bytes = [];

//     for (const byte of input_bytes) {
//         const xor_byte = byte ^ key;
//         output_bytes.push(xor_byte);
//     }

//     return output_bytes;
// }

// function decipher(encrypted_bytes) {
//     const key = 42;
//     const decrypted_bytes = [];

//     for (const byte of encrypted_bytes) {
//         const original_byte = byte ^ key;
//         decrypted_bytes.push(original_byte);
//     }

//     return decrypted_bytes;
// }

// // Example usage:
// const message = "6d5f5e4f0a6b58484f435e0b0a6e434f0a6b445e5d45585e0a464b5f5e4f5e0a6b6f7904";
// // const bytes = ascii_string_to_bytes(message);
// // console.log(bytes);// You need to define the function ascii_string_to_bytes
// // const encrypted_bytes = cipher(bytes);
// const decrypted_bytes = decipher(message);

// // Convert decrypted bytes back to string
// const decrypted_message = String.fromCharCode(...decrypted_bytes);

// console.log(decrypted_message);

// function ascii_string_to_bytes(input_string) {
//     const bytes = [];
//     for (let i = 0; i < input_string.length; i++) {
//         bytes.push(input_string.charCodeAt(i));
//     }
//     return bytes;
// }