#!/usr/bin/bash

rm -rf output

hadoop jar /usr/lib/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar \
      -input ./iris.data \
      -output ./output \
      -mapper ./mapper.py \
      -reducer ./reducer.py \

# cat iris.data | ./mapper.py | sort | ./reducer.py
