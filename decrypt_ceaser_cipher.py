def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - key) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

ciphertext = "ZDOFKDQGLQVWLWXWHRIWHFKQRORJB"
key = 3

decrypted_text = caesar_decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)
