#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10
output = f"Last digit of {number} is {num}"
if num > 5:
    output += " and is greater than 5"
elif num == 0:
    output += " and is 0"
else:
    output += " and is less than 6 and not 0"

print(output)
