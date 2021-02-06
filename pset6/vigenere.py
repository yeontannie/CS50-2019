from cs50 import get_string
from sys import argv
import sys

if len(argv) != 2:
    print("Usage: python vigenere.py keyword")
    exit(1)

if len(argv) == 2:
    keyword = argv[1]

    if keyword[0] == "H":
        print("Usage: python vigenere.py keyword")
        exit(1)


    if keyword.isalpha:
        s = get_string("plaintext: ")
        print("ciphertext: ", end="")
        j = 0

        for c in s:
            if not c.isalpha():
                print(c, end="")
                continue

            asci = 65 if c.isupper() else 97

            pi = ord(c) - asci
            kj = ord(keyword[j % len(keyword)].upper()) - 65
            ci = (pi + kj) % 26
            j += 1

            print(chr(ci + asci), end="")
        print()
