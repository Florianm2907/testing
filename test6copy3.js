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

function decipher(encrypted_hex_string, key) {
    
    const encrypted_bytes = convert_hex_string_to_bytes(encrypted_hex_string);
    const decrypted_bytes = [];
    let previousOutput = 0
    for (const byte of encrypted_bytes) {
        // const current_key = previousOutput ^ key;
        const xor_byte = byte ^ key;
        previousOutput = byte;
        decrypted_bytes.push(xor_byte);
    }

    // Convert decrypted bytes back to string
    const textDecoder = new TextDecoder('utf-8');
    const decrypted_message = textDecoder.decode(new Uint8Array(decrypted_bytes));

    return decrypted_message;
}
const encrypted_hex_string = "6d5f5e4f0a6b58484f435e0b0a6e434f0a6b445e5d45585e0a464b5f5e4f5e0a6b6f7904"
console.log(decipher(encrypted_hex_string, 42))