#!/usr/bin/python3
from sys import argv
length = len(argv)
if length == 1:
    print("0 arguments.")
else:
    if length == 2:
        print(f"{length - 1} argument:")
    else:
        print(f"{length - 1} arguments:")
    for idx in range(1, length):
        print(f"{idx}: {argv[idx]}")
