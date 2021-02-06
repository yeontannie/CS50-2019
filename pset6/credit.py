from cs50 import get_int

num = 0
tsum = 0
sumt = 0
counter = 0

while num < 1:
    num = get_int("Number: ")

# indicates first number of credit card
first = num
while first >= 100:
    first //= 10

# Lun's algorithm
sec = num
while sec > 10:
    thi = ((sec % 100) // 10) * 2

    if thi <= 9:
        tsum = thi + tsum;
    elif thi >= 10:
        n = thi;
        dec = thi;
        dec %= 10;
        n //= 10;
        tsum = dec + n + tsum;
    sec //= 100

fo = num
while fo > 1:
    fi = fo % 10
    sumt = fi + sumt
    fo //= 100

sum = tsum + sumt

# Indicates credit card
if sum % 10 == 0:

    while num > 0:
        num //= 10
        counter += 1

    if counter == 15 and first == 34 or first == 37:
        print("AMEX")

    if counter == 16 and first >= 51 and first <= 55:
        print("MASTERCARD")

    if counter >= 13 and counter <= 16 and first >= 40 and first <= 49:
        print("VISA")

else:
    print("INVALID")