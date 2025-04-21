"""
Helper module to generate value sequences
"""

__author__ = "Sachin Kharel"

import random


def sequence(max: int) -> list[int]:
    return list(range(max))


def random_sequence(max: int) -> list[int]:
    values: list[int] = sequence(max)

    for x in range(len(values)):
        y = random.randint(0, max-1)
        z = values[x]
        values[x] = values[y]
        values[y] = z

    return values