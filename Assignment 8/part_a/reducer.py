#!/usr/bin/env python3
"""reducer.py
With help from
https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/"""

import sys
from typing import Optional, List


# input comes from STDIN
for line in sys.stdin:
    print(line.strip())
