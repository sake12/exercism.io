import re


def is_isogram(text):
    word = re.sub('[^a-zA-Z]+', '', str.lower(text))
    for char in word:
        if word.count(char) > 1:
            return False
    return True
