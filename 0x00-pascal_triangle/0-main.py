#!/usr/bin/python3
"""
0-main
""" 
import time
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    start = time.time()
    print_triangle(pascal_triangle(500))
    end = time.time()
    print("the total run time is - ", end - start)
