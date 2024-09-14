#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i in range(len(line)):
            s = "{:d} "
            if i == 2:
                s = "{:d}"
            print(s.format(line[i]), end="")

        print()
