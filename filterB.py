#!/usr/bin/env python
"""
A filter that change uper characters into lower  characters.
"""

import fileinput


def process(line):
"""For each line of input, every words will be changed into lower characters."""
    print(line[:-1].lower())   


for line in fileinput.input():
    process(line)
