# Program to generate a random number between 0 and 9
# importing the random module
import requests


r = requests.get("https://google.com")
print(r.status_code)
print(r.ok)

# test()