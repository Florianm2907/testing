function decipher(encrypted_hex_string, key) {
    
    const encrypted_bytes = convert_hex_string_to_bytes(encrypted_hex_string);
    const decrypted_bytes = [];
    let previousOutput = 0
    for (const byte of encrypted_bytes) {
        const current_key = previousOutput ^ key;
        const xor_byte = byte ^ current_key;
        previousOutput = byte;
        decrypted_bytes.push(xor_byte);
    }

    // Convert decrypted bytes back to string
    const textDecoder = new TextDecoder('utf-8');
    const decrypted_message = textDecoder.decode(new Uint8Array(decrypted_bytes));

    return decrypted_message;
}


encrypted_hex_string = "4c2f513f5a3256355d3e577a1e60193458204e2b066f0b631d750a27690d70157d022f4c2846235a771b740a68097108255b3f51345c23002d680c641b365f3753305875395a23593b443d0a27781c6206600221"
let key = 0
for (key = 0; key < 256; key++){
    setTimeout((key) => {
        // console.clear()
        let decrypted_message = decipher(encrypted_hex_string, key);
        console.log("Key: " + key + ", Decrypted: " + decrypted_message);
    }, key * 500, key);
}

function convert_hex_string_to_bytes(hex_string) {
    const bytes = [];
    for (let i = 0; i < hex_string.length; i += 2) {
        bytes.push(parseInt(hex_string.substr(i, 2), 16));
    }
    return bytes;
}