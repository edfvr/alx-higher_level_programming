#!/usr/bin/python3
for c in range(97, 123):
    if c != 'q' and c != 113:
        print("{:c}".format(c), end="")
