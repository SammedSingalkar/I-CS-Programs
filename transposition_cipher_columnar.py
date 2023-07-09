#Columnar Transposition involves writing the plaintext out in rows, and then reading the ciphertext off in columns one by one
def encrypt_transposition(message, key):
    # Remove any whitespace from the message
    message = message.replace(" ", "")

    # Calculate the number of rows needed
    num_rows = len(message) // key
    if len(message) % key != 0:
        num_rows += 1

    # Create an empty grid to hold the encrypted message
    grid = [[''] * key for _ in range(num_rows)]

    # Fill the grid with the message by column
    col, row = 0, 0
    for char in message:
        grid[row][col] = char
        row += 1
        if row == num_rows:
            row = 0
            col += 1

    # Build the encrypted message by reading the grid row by row
    encrypted_message = ''
    for row in grid:
        encrypted_message += ''.join(row)

    return encrypted_message

# Test the encryption
message = "CRYPTANALYSISOFTRANSPOSITION CIPHERSISTOUGH"
key = 3
encrypted_message = encrypt_transposition(message, key)
print("Encrypted message:", encrypted_message)
