from cs50 import get_int

height = 0

while height <= 0 or height > 8:
    height = get_int("Height: ")

for i in range(height):
    j = height - i
    while j > 1:
        print(" ", end="")
        j -= 1
    for hash in range(i + 1):
        print("#", end="")
        hash += 1
    print()
    i += 1