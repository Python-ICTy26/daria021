import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(plaintext)):
        if plaintext[i] in alphabet:
            ind = alphabet.find(plaintext[i])
            ciphertext += alphabet[(ind + shift) % 26]
        elif plaintext[i] in alphabet_lower:
            ind = alphabet_lower.find(plaintext[i])
            ciphertext += alphabet_lower[(ind + shift) % 26]
        else:
            ciphertext += plaintext[i]

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(ciphertext)):
        if ciphertext[i] in alphabet:
            ind = alphabet.find(ciphertext[i])
            plaintext += alphabet[(ind - shift) % 26]
        elif ciphertext[i] in alphabet_lower:
            ind = alphabet_lower.find(ciphertext[i])
            plaintext += alphabet_lower[(ind - shift) % 26]
        else:
            plaintext += ciphertext[i]
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    for best_shift in range(26):
        if decrypt_caesar(ciphertext) in dictionary:
            return best_shift
