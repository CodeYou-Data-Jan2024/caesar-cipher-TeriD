# Define the lowercase and uppercase letters
alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = alphabet_lower.upper()

# Shift the alphabets by 5 using modular arithmetic
shifted_alphabet_lower = alphabet_lower[5:] + alphabet_lower[:5]
shifted_alphabet_upper = alphabet_upper[5:] + alphabet_upper[:5]

# Input text to encrypt
plaintext = input("Enter the text to encrypt: ")

# Encryption process
encrypted_text = ""
for char in plaintext:
    # Check if the letter is an alphabet letter
    if char.isalpha():
        # Check if the letter is uppercase
        if char.isupper():
            # Find the index of the letter in the original alphabet
            index = alphabet_upper.find(char)
            # Apply the shift and handle wrapping using modular arithmetic
            encrypted_char = shifted_alphabet_upper[index % 26]
            # Append the encrypted character to the result
            encrypted_text += encrypted_char
        else:
            # Find the index of the letter in the original lowercase alphabet
            index = alphabet_lower.find(char)
            # Apply the shift and handle wrapping using modular arithmetic
            encrypted_char = shifted_alphabet_lower[index % 26]
            # Append the encrypted character to the result
            encrypted_text += encrypted_char
    else:
        # If the character is not an alphabet letter, keep it unchanged
        encrypted_text += char

# Output the encrypted text
print("Encrypted:", encrypted_text)

