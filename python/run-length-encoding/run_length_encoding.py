from collections import Counter


def read_number(text):
    num = ''
    for char in text:
        if char.isdigit():
            num += char
        else:
            break
    return int(num)


def decode(text):
    number = 0
    position = 0
    ret = []

    while position < len(text):
        char = text[position]

        if char.isdigit():
            number = read_number(text[position:])  # read number no matter how long it is
            position += len(str(number))  # move 'position' behind the number
        else:
            if number:
                ret.append(number * char)  # 'change' number and char into string
                number = 0
            else:
                ret.append(char)

            position += 1

    return ''.join(ret)


def read_length(text, char):
    number = 0
    for a in text:
        if a == char:
            number += 1
        else:
            break
    return number


def encode(text):
    position = 0
    ret = []

    while position < len(text):
        char = text[position]  # read current char
        length = read_length(text[position:], char)  # check how many times char is repeating

        if length == 1:
            ret.append(char)  # don't need to put number
        else:
            ret.append(str(length) + char)

        position += length

    return ''.join(ret)
