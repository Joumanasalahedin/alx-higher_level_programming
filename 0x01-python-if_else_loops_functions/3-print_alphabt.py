#!/usr/bin/python3
for letter in range(ord('a'), ord('z') + 1):
    if letter not in [101, 113]:
        print("{:c}".format(letter), end="")
