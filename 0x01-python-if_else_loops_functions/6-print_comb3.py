#!/usr/bin/python3
# YOUR CODE HERE
for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            if i != 8 or j != 9:
                print("{}{}, ".format(i, j), end="")

print("89")
