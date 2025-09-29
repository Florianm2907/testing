from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return ciphertext

def aes_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()

if __name__ == "__main__":
    # 128-bit key (16 bytes)
    key = bytes.fromhex("786d229b0de877774a2f676d5bd895c3")

    # Input plaintext
    plaintext = '{"player":"John","gold":999999}'

    # Encrypt the plaintext
    ciphertext = aes_encrypt(key, plaintext)
    print("Ciphertext:", ciphertext.hex())
    # print(type(ciphertext))
    # Decrypt the ciphertext
    # key = "786d229b0de877774a2f676d5bd895c3"
    # text = "cc76663b7d1e97ea2455b1c25676f44794fec90b0a9b823f916bf79387de4238"
    decrypted_text = aes_decrypt(key, ciphertext)
    print("Decrypted Text:", decrypted_text)

# from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad

# def aes_decrypt(key, ciphertext):
#     cipher = AES.new(key, AES.MODE_ECB)
#     plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
#     return plaintext.decode()

# if __name__ == "__main__":
#     # Input the 128-bit key as a hexadecimal string
#     key_hex = input("Enter the 128-bit AES key in hexadecimal format (32 characters): ")
#     key_hex = "786d229b0de877774a2f676d5bd895c3"
#     key = bytes.fromhex(key_hex)
#     # Input the ciphertext as a hexadecimal string
#     ciphertext_hex = input("Enter the ciphertext in hexadecimal format: ")
#     ciphertext_hex = "cc76663b7d1e97ea2455b1c25676f44794fec90b0a9b823f916bf79387de4238"
#     ciphertext = bytes.fromhex(ciphertext_hex)

#     # Decrypt the ciphertext
#     decrypted_text = aes_decrypt(key, ciphertext)
#     print("Decrypted Text:", decrypted_text)
