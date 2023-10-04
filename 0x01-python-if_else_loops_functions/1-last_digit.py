#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Code gets the last digit of the number
last_digit = abs(number) % 10

# checks if the last digit is greater than 5, 0, or less than 6 and not 0
if number < 0:
    last_digit *= -1

# code prints the output based on the conditions
print(f"Last digit of {number} is {last_digit} and", end=" ")

if last_digit > 5:
    print("is greater than 5")
elif last_digit == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")
