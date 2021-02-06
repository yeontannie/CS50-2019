def lines(a, b):
    """Return lines in both a and b"""

    aln = set(a.split("\n"))
    bln = set(b.split("\n"))

    return aln & bln

def sentences(a, b):
    from nltk.tokenize import sent_tokenize
    """Return sentences in both a and b"""

    asn = set(sent_tokenize(a))
    bsn = set(sent_tokenize(b))

    return asn & bsn

def substr_token(str, n):

    substr = []

    for i in range(len(str) - n + 1):
        substr.append(str[i:i + n])

    return substr

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    ass = set(substr_token(a, n))
    bss = set(substr_token(b, n))

    return ass & bss
