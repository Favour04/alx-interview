#!/usr/bin/python3
"""
    This module contain functions
    which will hepl in hetting pascal triangle
"""


def f(num):
    """
        This fuction is used to get the factorial of a number
        given to it
    """
    if num == 0:
        return 1

    if num <= 1:
        return num
    else:
        return num * f(num - 1)


def pascal_triangle(num):
    """
        The function generate a pascal triangle
    """
    if num == 0:
        return []
    if num == 1:
        return [[1]]
    pascals = []
    for i in range(num):
        fac = list(map(lambda n: int(f(i) / (fc(i - n) * f(n))), range(i + 1)))
        pascals.append(fac)

    return pascals
