#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for raw in matrix:
        if len(raw) == 0:
            print()
        for i in range(len(raw)):
            print("{:d}".format(raw[i]), end="\n" if i is len(raw) - 1 else " ")
