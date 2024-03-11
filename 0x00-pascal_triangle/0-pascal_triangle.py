#!/usr/bin/python3
""" Pascal's Triangle"""


def pascal_triangle(num):
    """
    Returns a list of list of integers
    representing the Pascal's triangle of 
    num
    """
    outer = []
    if num > 0:
        for idx in range(1, num+1):
            inner = []
            x = 1
            for jdx in range(1, idx + 1):
                inner.append(x)
                x = x * (idx - jdx) // jdx
            outer.append(inner)
    return outer
