#!/usr/bin/env python3
"""reducer.py
With help from
https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/"""

import sys
from typing import Optional, List

last_word: Optional[str] = None
last_count = 0

# input comes from STDIN
for line in sys.stdin:
    words = line.split("\t")
    word, count = words[0].strip(), int(words[1])

    if last_word == word:
        last_count += count
    else:
        print(last_word, last_count, sep="\t")
        last_word = word
        last_count = count
