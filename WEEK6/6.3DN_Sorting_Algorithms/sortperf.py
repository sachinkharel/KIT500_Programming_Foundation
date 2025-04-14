"""
Utility for comparing the runtime of various sorting algorithms.
Part of 6.3DN Sorting Algorithms.
"""

__author__ = "Sachin Kharel"

from enum import Enum
import random
import timeit

import listroutines


class Alg(Enum):
    """
    Supported algorithms.
    """
    SELECT = "Selection Sort"
    INSERT = "Insertion Sort"
    POWERS = "Powersort"
    BUBBLE = "Bubble Sort" # added bubble sort for comparison


def generate_random_list(size: int, lo: int, hi: int) -> list[int]:
    """
    Creates a list of size elements randomly initialised between lo and hi, inclusive.
    """
    l: list[int] = []
    for _ in range(size):
        l.append(random.randint(lo, hi))
    return l


def generate_sequential_list(size: int) -> list[int]:
    """
    Creates a list of size elements containing the values [1, 2, ... size].
    """
    l: list[int] = []
    for i in range(size):
        l.append(i+1)
    return l


def compare_algs_random(size: int, lo: int, hi: int, display: bool):
    """
    Compares all supported sorting algorithms on randomised data in range [lo, hi].
    """
    compare_algs(generate_random_list(size, lo, hi), display)


def compare_algs_sorted(size: int, display: bool):
    """
    Compares all supported sorting algorithms on sequential data.
    """
    compare_algs(generate_sequential_list(size), display)


def compare_algs(data: list[int], display: bool):
    """
    Compares all supported sorting algorithms on the given list of integers, optionally
    displaying their results after to confirm they all achieve the same outcome.
    """
    select_sorted = list(data)
    insert_sorted = list(data)
    powers_sorted = list(data)
    bubble_sort = list(data)

    print(f"Sorting {len(data)} items to compare sorting algorithm performance... ", end="")
    select_time = timed_sort(select_sorted, Alg.SELECT)
    insert_time = timed_sort(insert_sorted, Alg.INSERT)
    powers_time = timed_sort(powers_sorted, Alg.POWERS)
    bubble_time = timed_sort(bubble_sort, Alg.BUBBLE) # added bubble sort for comparison
    print("done")

    if display:
        print("Original data:")
        listroutines.display(data)
        print("Data sorted by\nSelect\tInsert\tPowersort")
        display_results(select_sorted, insert_sorted, powers_sorted, bubble_sort)
        print()

    print(f"Time to sort {len(data)} elements:")
    display_timing(f"{Alg.SELECT.value}:\t", select_time)
    display_timing(f"{Alg.INSERT.value}:\t", insert_time)
    display_timing(f"{Alg.POWERS.value}:\t", powers_time)
    display_timing(f"{Alg.BUBBLE.value}:\t", bubble_time) # added bubble sort for comparison


def timed_sort(data: list[int], algorithm: Alg) -> float:
    """
    Returns how long it took to sort the list data using the named algorithm.
    """
    start = timeit.default_timer()
    match algorithm:
        case Alg.SELECT:
            listroutines.selection_sort(data)
        case Alg.INSERT:
            listroutines.insertion_sort(data)
        case Alg.POWERS:
            data.sort()
        case Alg.BUBBLE:
            listroutines.bubble_sort(data) # added bubble sort for comparison
    stop = timeit.default_timer()
    return stop - start


def display_timing(prefix: str, time: float):
    """
    Displays the given time formatted as milliseconds, seconds, and minutes.
    """
    print(f"{prefix}{time*1000:2.1f} ms\tor\t{time:2.1f} s\tor\t{time/60:2.1f} min")


def display_results(*data: list[int]):
    """
    Displays the contents of 0 or more lists (of the same length) side by side.
    """
    for i in range(len(data[0])):
        for res in data:
            print(f"{res[i]}", end="\t")
        print()


def main():
    LBOUND = 0
    UBOUND = 1000
    SIZE = 4200
    # compare_algs_random(SIZE, LBOUND, UBOUND, True)
    compare_algs_sorted(SIZE, True)


if __name__ == "__main__":
    main()
