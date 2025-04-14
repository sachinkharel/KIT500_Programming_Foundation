"""
A collection of sorting algorithms for comparison with in-built sorting functions.
"""

__author__ = "James Montgomery, Lawrence Sambrooks, Sachin Kharel"


def insertion_sort(data: list[int]):
    """
    Sorts the list into ascending order using insertion sort.
    See this Wikipedia article: https://en.wikipedia.org/wiki/Insertion_sort
    """
    key: int # value to "insert"
    position: int # where to "insert"

    for i in range(1, len(data)):
        key = data[i]
        position = i
        # Shift larger values to the right
        while position > 0 and data[position-1] > key:
            position -= 1
        data.insert(position, data.pop(i))


def selection_sort(data: list[int]):
    """
    Sorts the list into ascending order using selection sort.
    See this Wikipedia article: https://en.wikipedia.org/wiki/Selection_sort
    """
    min: int
    temp: int

    for i in range(0, len(data)-1):
        min = i
        for scan in range(i+1, len(data)):
            if data[scan] < data[min]:
                min = scan
        # Swap the values
        data[min], data[i] = data[i], data[min]

def bubble_sort(data: list[int]):
    """
    Sorts the list into ascending order using bubble sort.
    See this Wikipedia article: https://en.wikipedia.org/wiki/Bubble_sort
    """
    temp: int # temp variable for swapping values
    
    for i in range(len(data)-1,0, -1): # indexing data backwards
        for j in range(0, i):
            if data[j] > data[j+1]:
                # Swap the values
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

def display(l: list[int]):
    """
    Displays the values stored in a list of ints.
    """
    for i, val in enumerate(l):
        print(f"element {i}: {val}") # the formatting is up to you
