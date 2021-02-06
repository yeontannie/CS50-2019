from cs50 import get_float
from math import ceil

dollars = 0
counter = 0

while dollars <= 0:
    dollars = get_float("Change Owed: ")
    if dollars >= 0.1:
        break

coins = ceil(dollars * 100)

while coins >= 25:
    coins -= 25
    counter += 1
while coins >= 10:
    coins -= 10
    counter += 1
while coins >= 5:
    coins -= 5
    counter += 1
while coins >= 1:
    coins -= 1
    counter += 1
print(f"I owe you: {counter}")