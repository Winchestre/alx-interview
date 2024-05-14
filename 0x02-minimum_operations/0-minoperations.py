#!/usr/bin/python3
""" Module Function """


def minOperations(n):
    """ Function Doc """
    if (n < 2):
        return 0
    operations, root = 0, 2
    while root <= n:
        if n % root == 0:
            operations += root
            n /= root
            root -= 1
        root += 1
    return operations
