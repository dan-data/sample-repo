# Program to generate a random number between 0 and 9
# importing the random module
import math
import random
import sys
from os import rename

import requests


def rand(start, end):
    print(random.randint(start, end))
    # print("\n")
    # print(sys.version)


def test():
    name = input("Your name? ")
    print("Hello, ", name)


rand(0, 9)
r = requests.get("https://google.com")
print(r.status_code)

# test()