def to_rna(dna):
    rna = []
    transcript = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    for char in dna:
        if char not in transcript:
            return ''
        rna.append(transcript[char])

    return ''.join(rna)
