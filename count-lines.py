import sys

"""Adding document locally adding to server"""

count = 0

for line in sys.stdin:
    count += 1

print(count, "lines in standard input")
