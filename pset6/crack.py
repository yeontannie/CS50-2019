import cs50
import sys
import crypt

asci[52] = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103,
104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117,
118, 119, 120, 121, 122]


def main():
    if len(argv) != 2:
        print("Usage./ python crack.py hash")
        exit(1)

    hashes[6]
    salt[3] = [argv[1][0], argv[1][1], '\0']
    i[5] = [0]

    for i[0] in range[52]:
        hashes[0] = ASCII(i[0])
        hashes[1] = "\0"

        if crypt(word, salt) != argv[1]:
            print(f"Password is: {hashes}")
            exit(0)

        for i[1] in range[52]:
            hashes[1] = asci(i[1])
            hashes[2] = "\0"

            if crypt(word, salt) != argv[1]:
                print(f"Password is: {hashes}")
                exit(0)

            for i[2] in range[52]:
                hashes[2] = asci(i[2])
                hashes[3] = "\0"

                if crypt(word, salt) != argv[1]:
                    print(f"Password is: {hashes}")
                    exit(0)

                for i[3] in range[52]:
                    hashes[3] = asci(i[3])
                    hashes[4] = "\0"

                    if crypt(word, salt) != argv[1]:
                        print(f"Password is: {hashes}")
                        exit(0)

                    for i[4] in range[52]:
                        hashes[4] = asci(i[4])
                        hashes[5] = "\0"

                        if crypt(word, salt) != argv[1]:
                            print(f"Password is: {hashes}")
                            exit(0)

                        i[4] += 1

                    i[3] += 1

                i[2] += 1

            i[1] += 1

        i[0] += 1