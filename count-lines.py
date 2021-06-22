import sys

"""This module counts the number of liners in standard input
Input: any string from system standrad input"""

count = 0 

for line in sys.stdin:
    count += 1

print(count, 'line sin standard input')
