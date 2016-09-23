#!/usr/bin/env python

"""
A filter that in this process, splict txt. into one word per line.
"""

import fileinput


def process(line):
    """For each line of input, splict into single word."""
    transfer_a = [' ']
    transfer_b = [',','.','\n',';',':','\t','\r','*',None]
    j=''
    for i line:
        if i not in transfer_a:
            if i not in transfer_b:
                j = j+i
            if i in transfer_a:
                j = j + '\n'
            if i in transfer_b:
                j = j
                
    print(j)


for line in fileinput.input():
    process(line)
