import string


def is_pangram(text):
    return not set(string.ascii_lowercase) - set(text.lower())
