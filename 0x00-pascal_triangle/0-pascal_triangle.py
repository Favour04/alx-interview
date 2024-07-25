#!/usr/bin/python3
"""
Get factorial of a number
"""


def f(num):
    """
        This fuction is used to get the factorial of a number
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
    pascals = []
    for i in range(num):
        fac = list(map(lambda n: int(f(i) / (f(i - n) * f(n))), range(i + 1)))
        pascals.append(fac)

    return pascals
