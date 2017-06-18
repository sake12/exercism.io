import re


def abbreviate(text):
    return "".join(item[0].upper() for item in re.findall("\w+", text))
