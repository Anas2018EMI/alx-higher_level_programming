#!/usr/bin/python3

result = ""
for i in range(122, 96, -1):
    if i % 2 == 0:
        result += "{}".format(chr(i))
    else:
        result += "{}".format(chr(i - 32))
print(result, end="")
