#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b))) #    10 + 5 = 15
    print("{} - {} = {}".format(a, b, sub(a, b))) #    10 - 5 = 5
    print("{} * {} = {}".format(a, b, mul(a, b))) #    10 * 5 = 50
    print("{} / {} = {}".format(a, b, div(a, b))) #    10 / 5 = 2
