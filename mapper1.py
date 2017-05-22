#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split(",")
    print '%s,%s,%s' % (words[4],words[11],1)