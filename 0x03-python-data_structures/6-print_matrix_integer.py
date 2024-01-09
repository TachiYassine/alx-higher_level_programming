#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for raw in matrix:
        for element in raw:
            print("{:d}".format(element), end=" ")  # Using end=" " to print elements in the same line
        print("")  # Printing a new line after each sublist
