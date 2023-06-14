#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    b_score = max(a_dictionary.values(), default=None)
    for j, f in a_dictionary.items():
        if f == b_score:
            return j
