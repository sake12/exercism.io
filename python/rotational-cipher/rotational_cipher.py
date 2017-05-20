from string import ascii_lowercase, ascii_uppercase

LENGTH = len(ascii_lowercase)


def rotate(text, rot):
    """
    Implementation of the rotational cipher, also sometimes called the Caesar cipher.
    :param text: Text to encode
    :param rot: How many places to rotate. 13 means rotate by 13 places.
    :return: Encoded text
    """
    ret = []
    for char in text:
        ret.append(convert(char, rot))
    return ''.join(ret)


def convert(char, rot):
    val = ord(char)
    if char in ascii_lowercase:
        return ascii_lowercase[(rot + ascii_lowercase.find(char)) % LENGTH]
    elif char in ascii_uppercase:
        return ascii_uppercase[(rot + ascii_uppercase.find(char)) % LENGTH]
    else:
        return chr(val)
