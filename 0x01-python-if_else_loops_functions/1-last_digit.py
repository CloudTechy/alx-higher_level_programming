#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = abs(number) % 10
if number < 0:
    n *= -1
if n == 0:
    print(f"Last digit of {number} is {n} and is 0")
elif n > 5:
    print(f"Last digit of {number} is {n} and is greater than 5")
else:
    print(f"Last digit of {number} is {n} and is less than 6 and not 0")
