import re


def hey(text):
    word = re.sub('[^a-zA-Z0-9?]+', '', text)

    if not word:
        return 'Fine. Be that way!'
    elif word.isupper():
        return 'Whoa, chill out!'
    elif word.endswith('?'):
        return 'Sure.'
    else:
        return 'Whatever.'
