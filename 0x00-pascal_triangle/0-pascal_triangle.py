#!/usr/bin/python3
"""
Get factorial of a number
"""
def factorial(num):
        if num == 0:
             return 1
        
        if num <= 1:
            return num
        else:
            return num * factorial(num - 1)

"""
generate pascal tiangle
"""
def pascal_triangle(num):
     pascals = []
     for i in range(num + 1):
          fac = list(map(lambda n: int(factorial(i) / (factorial(i - n) * factorial(n))), range(i + 1)))
          pascals.append(fac)
     return pascals
