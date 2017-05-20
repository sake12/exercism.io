def distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError

    hamming = 0

    for pos1, pos2 in zip(str1, str2):
        if pos1 != pos2:
            hamming += 1

    return hamming
