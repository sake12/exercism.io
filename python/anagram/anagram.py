def detect_anagrams(text, candidates):
    """Given a word and a list of possible anagrams, returns anagrams of that word."""
    ret = []
    main = text.lower()
    sort = sorted(main)
    for word in candidates:
        check = word.lower()

        if main == check:
            continue

        if sort == sorted(check):
            ret.append(word)
    return ret
