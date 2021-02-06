from cs50 import get_string
from sys import argv
import sys

def main():
    if len(argv) != 2:
        print("Usage./ python bleep.py dictionary")
        exit(1)

    if argv[1].find(".txt") == 0:
        print("Usage./ python bleep.py dictionary")
        exit(1)


    words = set()

    #makes dictionary
    file = open(argv[1], "r")
    if file == 0:
        file.close()
        print(f"Could not open {argv[1]}")
        exit(1)

    for line in file:
        words.add(line.rstrip("\n"))
    file.close()

    #get input
    print("What message would you like to censor?")
    s = get_string("")
    s = s.split()

    for c in s:
        i = c
        c = c.lower()
        if not c in words:
            print(i , end=" ")
            continue

        if c in words:
            print("*" * len(c), end=" ")
            continue

    print()

if __name__ == "__main__":
    main()
