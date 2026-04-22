# Vigenere Cipher

def encrypt(text, key):
    result = ""
    key = key.lower()
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 97
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(cipher, key):
    result = ""
    key = key.lower()
    for i in range(len(cipher)):
        char = cipher[i]
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 97
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

text = "hello"
key = "key"

encrypted = encrypt(text, key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypt(encrypted, key))
