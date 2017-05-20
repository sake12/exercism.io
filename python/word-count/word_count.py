from collections import Counter


def word_count(text):
    words = ''.join(c.lower() if c.isalnum() else ' ' for c in text).split()

    return Counter(words)
