#!/usr/bin/bash

# cd "/home/ujjwal/courses/IT Workshop 3/Assignments/Assignment 7"

hadoop jar /usr/lib/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar \
      -input ./big.txt \
      -output ./output \
      -mapper ./mapper.py \
      -reducer ./reducer.py \

# cat big.txt | ./mapper.py | sort -t \t -k1 | ./reducer.py