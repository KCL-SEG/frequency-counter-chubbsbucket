"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if not isinstance(item, str):
            item = str(item)
        if(frequencies.get(item)):
            frequencies[item] = frequencies[item] + 1
        else:
            frequencies[item] = 1
    else:
        return frequencies