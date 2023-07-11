#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    count = 0
    for idx in str:
        if count != n:
            copy += idx
        count += 1
    return copy
