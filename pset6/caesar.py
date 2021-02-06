from sys import argv
from cs50 import get_string

if len(argv) == 2:
    key = int(argv[1])

    if key == 0:
        print("Usage: python caesar.py key")
        exit(1)

    else:
        s = get_string("plaintext: ")
        print("ciphertext: ", end="")

        for i in range(len(s)):
            c = ord(s[i])

            if c >= 97 and c <= 122 or c >= 65 and c <= 90:

                if c >= 97 and c <= 122:
                    c += key

                    while c >= 123:
                        c -= 122
                        c += 96

                if c >= 65 and c <= 90:
                    c += key

                    while c >= 91:
                        c -= 90
                        c += 64

                a = chr(c)
                print(a, end="")

            else:
                b = chr(c)
                print(b, end="")

        i += 1
    print()

if len(argv) != 2:
    print("Usage: python caesar.py key")
    exit(1)
