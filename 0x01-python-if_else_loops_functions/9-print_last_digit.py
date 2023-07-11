#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    if number < 0:
        last_digit = -last_digit
    print(last_digit)


print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
