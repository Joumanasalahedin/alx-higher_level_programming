#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
sum = 0
idx = 0
for arg in argv:
    if idx != 0:
        sum += int(arg)
    idx += 1
print(sum)
