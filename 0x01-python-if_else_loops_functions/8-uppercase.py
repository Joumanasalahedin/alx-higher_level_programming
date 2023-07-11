#!/usr/bin/python3
def uppercase(str):
    new = ""
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = chr(ord(letter) - 32)
        new += letter
    print("{}".format(new))
