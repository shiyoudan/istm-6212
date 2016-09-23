#!/usr/bin/env python

"""
A filter that count and remove top25 words.
"""

import fileinput


def process(line):
    """For each line of input, _____."""
    def remove_stop_word(lower_words,n=25):
    words = lower_words.split('\n')
    words_count = dict()
    for word in words:
      if word in words_count:
        words_count[word]+=1
      else:
        words_count[word]=1
    sort_words = sorted(words_count.items(),key=lambda x:x[1],reverse=True)
    stop_word = set()
    for word in sort_words[:n]:
        stop_word.add(word[0])
        print (word[0],word[1])
    result = []
    for word in words:
       if word in stop_word:
         continue
       else:
         result.append(word)
    return '\n'.join(result)


for line in fileinput.input():
    process(line)
