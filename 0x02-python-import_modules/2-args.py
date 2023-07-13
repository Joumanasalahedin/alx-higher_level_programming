#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
length = len(argv) - 1
if length == 0:
    print("0 arguments.")
else:
    if length == 1:
        print(f"{length} argument:")
    else:
        print(f"{length} arguments:")
    idx = 0
    for arg in argv:
        if idx != 0:
            print(f"{idx}: {arg}")
        idx += 1
