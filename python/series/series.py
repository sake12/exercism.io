def slices(text, number):
    """
    Given a string of digits, output all the contiguous substrings
    of length 'number' in that string.
    """
    ret = []
    if not (1 <= number <= len(text)):
        raise ValueError("No way I can do it!")

    for X in range(len(text)):
        slc = text[X:X+number]
        if len(slc) != number:
            break

        ret.append([int(a) for a in slc])

    return ret
