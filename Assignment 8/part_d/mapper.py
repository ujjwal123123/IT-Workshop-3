#!/usr/bin/env python3
"""mapper.py
With help from
https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
"""

import sys
from string import punctuation

with open("stopwords.txt", "r") as f:
    stop_words = f.read().split("\n")

byte_offset = 0

for line in sys.stdin:
    line = line.strip().lower()
    words: list[str] = line.split()

    for word in words:
        new_word = word.strip().strip(punctuation)
        if (
            new_word
            and new_word not in stop_words
            and "-" not in new_word
            and "." not in new_word
            and "," not in new_word
            and "[" not in new_word
            and "]" not in new_word
            and "/" not in new_word
        ):
            print(f"{new_word}\t{byte_offset}")

        byte_offset += len(word) + 1
