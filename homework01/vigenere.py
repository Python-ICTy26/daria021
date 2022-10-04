def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(plaintext)):
        if plaintext[i] in alphabet:
            ind = alphabet.find(plaintext[i])
            shift = alphabet.find(keyword[i % len(keyword)])
            ciphertext += alphabet[(ind + shift) % 26]
        else:
            ind = alphabet_lower.find(plaintext[i])
            shift = alphabet_lower.find(keyword[i % len(keyword)])
            ciphertext += alphabet_lower[(ind + shift) % 26]

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(ciphertext)):
        if ciphertext[i] in alphabet:
            ind = alphabet.find(ciphertext[i])
            shift = alphabet.find(keyword[i % len(keyword)])
            plaintext += alphabet[(ind - shift) % 26]
        else:
            ind = alphabet_lower.find(ciphertext[i])
            shift = alphabet_lower.find(keyword[i % len(keyword)])
            plaintext += alphabet_lower[(ind - shift) % 26]

    return plaintext
