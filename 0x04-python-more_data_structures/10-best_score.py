#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    best_key = None

    if a_dictionary is None:
        return None
    for key, value in a_dictionary.items():
        if value > best:
            best = value
            best_key = key

    return best_key
