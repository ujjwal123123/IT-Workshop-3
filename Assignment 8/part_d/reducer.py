#!/usr/bin/env python3
"""reducer.py
With help from
https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/"""

from os import error
import sys
from typing import Optional, List

current_word: Optional[str] = None
current_set: set[int] = set()

for line in sys.stdin:
    line_new: List[str] = line.strip().split("\t")
    assert len(line_new) == 2

    word = line_new[0]
    byte_offset: int = int(line_new[1])

    if current_word == word:
        current_set.add(byte_offset)
    else:
        if current_word:
            print(current_word, current_set, sep="\t")
        current_word = word
        current_set = {byte_offset}

if current_word:
    print(current_word, current_set, sep="\t")
