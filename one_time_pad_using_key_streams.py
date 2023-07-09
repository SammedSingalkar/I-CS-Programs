def otp_encrypt(message, key):
    ciphertext = ""
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            key_shift = key[i] % 26
            encrypted_char = chr((ord(char) - ascii_offset + key_shift) % 26 + ascii_offset)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def otp_decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            key_shift = key[i] % 26
            decrypted_char = chr((ord(char) - ascii_offset - key_shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def main():
    message = "sendmoremoney"
    key = [8, 12, 1, 7, 23, 15, 21, 14, 11, 19, 2, 0, 9]

    # Encrypt the message
    encrypted_message = otp_encrypt(message, key)
    print("Encrypted Message:", encrypted_message)

    # Decrypt the ciphertext
    decrypted_message = otp_decrypt(encrypted_message, key)
    print("Decrypted Message:", decrypted_message)

if __name__ == '__main__':
    main()
