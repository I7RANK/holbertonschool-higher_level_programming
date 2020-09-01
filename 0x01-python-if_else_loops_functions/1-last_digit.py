#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10

if number < 0 and last != 0:
    last = last - 10

print("Last digit of {0} is {1} and is".format(number, last), end="")

if last == 0:
    print(" 0")
elif last > 5:
    print(" greater than 5")
else:
    print(" less than 6 and not 0")
