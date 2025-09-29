import time
import os

# The given cipher_ii function
def cipher_ii(input_bytes, key):
    previousOutput = 0
    output_bytes = []

    for byte in input_bytes:
        current_key = previousOutput ^ key
        xor_byte = byte ^ current_key
        previousOutput = byte
        output_bytes.append(xor_byte)

    return bytes(output_bytes)

# Function to convert hex string to bytes
def hex_string_to_bytes(hex_string):
    return bytes.fromhex(hex_string)

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Define your encrypted hex string
encrypted_hex_string = "4c2f513f5a3256355d3e577a1e60193458204e2b066f0b631d750a27690d70157d022f4c2846235a771b740a68097108255b3f51345c23002d680c641b365f3753305875395a23593b443d0a27781c6206600221"  # Replace with your actual encrypted message

encrypted_bytes = hex_string_to_bytes(encrypted_hex_string)

# Brute-force keys from 0 to 256
for key in range(256):
    clear_console()
    print(f"Trying Key: {key}")
    
    decrypted_bytes = cipher_ii(encrypted_bytes, key)
    decrypted_message = decrypted_bytes.decode('utf-8', errors='ignore')
    
    print(f"Decrypted Message with Key {key}: {decrypted_message}")
    
    time.sleep(1)
