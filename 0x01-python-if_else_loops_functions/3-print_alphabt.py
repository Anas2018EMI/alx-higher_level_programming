#!/usr/bin/python3
# YOUR CODE HERE
for i in range(ord('a'), ord('z')+1):
    if i != ord('e') and i != ord('q'):
        print("{}".format(chr(i)), end="")
