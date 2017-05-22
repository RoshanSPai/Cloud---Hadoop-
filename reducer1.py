#!/usr/bin/env python
import sys

current_word1 = None
current_word2 = None
current_count = 0
words=[]
for line in sys.stdin:
    line.strip()
    words = line.split(',')
    # convert count (currently a string) to int
    try:
        count = int(words[2])
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if (current_word1 == words[0] and current_word2 == words[1]):
        current_count += count
    else:
        if current_word1:
        # write result to STDOUT
            print '%s,%s,%s' % (current_word1,current_word2, current_count)
        current_count = count
        current_word1 = words[0]
        current_word2 = words[1]
# do not forget to output the last word if needed!
if current_word1 == words[0] and current_word2 == words[1]:
    print '%s,%s,%s' % (current_word1,current_word2,current_count)
