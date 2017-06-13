from string import ascii_lowercase

LENGTH = len(ascii_lowercase)
BEGINNING = ord('a') - 1


def cipher(text):
    """Implementation of the atbash cipher, an ancient encryption system created in the Middle East."""
    ret = []

    for char in text.lower():
        if char.isdigit():
            ret.append(char)
        elif char.isalpha():
            ret.append(ascii_lowercase[(BEGINNING - ord(char)) % LENGTH])

    return [''.join(ret[x:x+5]) for x in range(0, len(ret), 5)]


def encode(text):
    """Encode text into the atbash cipher"""
    return ' '.join(cipher(text))


def decode(text):
    """Decode text from the atbash cipher"""
    return ''.join(cipher(text))
