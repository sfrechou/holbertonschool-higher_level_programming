#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """returns list of lists of integers - Pascal's triangle"""
    totallist = []
    if n <= 0:
        return totallist
    for row in range(0, n):
        rows = []
        for a in range(0, row + 1):
            result = 1
            b = a
            k = row
            if b > k - b:
                b = k - b
            for c in range(0, b):
                result = result * (k - c)
                result = result // (c + 1)
            rows.append(result)
        totallist.append(list(rows))
    return totallist
