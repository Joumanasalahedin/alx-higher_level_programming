#!/usr/bin/python3
""" Module with function that prints a text with
2 new lines after certain characters """


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after
    . ? and :

    Args:
    text: string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for d in ".?:":
        text = (d + "\n\n").join(
            [line.strip(" ") for line in text.split(d)])

    print(f"{text}", end="")
