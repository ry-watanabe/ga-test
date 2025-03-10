import sys
import random

import math


def greet(name):
    message = "Hello, " + name
    print(message)


name = "Alice"
greet(name)


def add_numbers(a, b):
    result = a + b
    return result


num1 = 5
num2 = 7
sum = add_numbers(num1, num2)
print("Sum:", sum)
