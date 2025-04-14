"""
Exception Play (10.1 Exception Handling)

A collection of code samples that will involve exception handling.
"""

__author__ = "Lawrence Sambrooks, James Montgomery, Sachin Kharel"


from enum import Enum
from io import IOBase
from os import path
from urllib.error import URLError
from urllib.request import urlopen

class MenuOption(Enum):
    """Program menu options"""
    NUMBER_INPUT = 1
    LIST_ACCESS = 2
    FILE_READING = 3
    WEBPAGE_READING = 4
    QUIT = 5


def confirm(prompt: str) -> bool:
    """Returns True if response is 'y', False if 'n'"""
    outcome = None

    while outcome is None:
        match input(f"{prompt} (y/n)? "):
            case "y": outcome = True
            case "n": outcome = False
            case _: print("Please respond y or n only")
    return outcome


def read_an_int(query: str) -> int:
    """Part of the number input and list access examples."""
    value: int = None # value obtained from the user
    while value is None:
        # added a try/except block to catch ValueError
        try:
            value = int(input(f"{query}: "))
        except ValueError:
            print("Cannot interpret input as a number")
    return value


def number_input():
    """Runs the number input and parsing example."""
    do_more = True
    collected: list[int] = [] #collection of all values entered by the user
    num: int #A number to read from the user

    print("\nNumber Parsing Example")
    while do_more:
        num = read_an_int("Enter an integer to add to the collection")
        collected.append(num)
        do_more = confirm("Add another?")
    print(f"You entered these valid integer values: {', '.join(map(str, collected))}")


def list_access():
    """Runs the list access example."""
    do_more = True
    data = [7, 3, 9, 2, 4]
    index: int #user's selected position to view

    print("\nList Access Example")
    while do_more:
        try:
            index = read_an_int("Enter an index to view: ")
            print(f"Value at position {index} is {data[index]}")
        except IndexError:
            print(f"Index {index} is out of range")
        do_more = confirm("Inspect another")


def read_display_close(readable: IOBase, description: str):
    """
    Reads from, displays and then closes the given input steam, which
    could be from a file or network connection: anything supporting read().
    Does not handle any reading errors.
    """
    full_contents = readable.read()
    print(description)
    print(full_contents)
    readable.close()


def read_file():
    """Runs the file reading example."""
    filename: str

    filename = input("Enter a file name in the current directory: ")
    try:
        read_display_close(open(f"{path.dirname(__file__)}/{filename}", "r"), f"Contents of {filename}:")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except UnicodeDecodeError:
        print(f"File {filename} is not a text file")


def read_webpage():
    """Runs the web page reading example."""
    url: str #URL as given by the user
    url = input("Enter the URL of a webpage: ")
    try:
        read_display_close(urlopen(url), f"Contents of {url}:")
    except ValueError as e:
       print(f"{e}")
    except URLError as e:
        print(f"{e}")

def main():
    choice: int # user's typed menu choice
    option: MenuOption = None # user's internal menu choice

    while option != MenuOption.QUIT:
        print("Exception Play")
        for option in MenuOption:
            print(f"{option.value}. {option.name.capitalize().replace("_", " ")}")
        choice = read_an_int("Selection")
        option = MenuOption(choice) if choice in MenuOption else None # clever if less readable way of converting their choice to an enum value
        match option:
            case MenuOption.NUMBER_INPUT:
                number_input()
            case MenuOption.LIST_ACCESS:
                list_access()
            case MenuOption.FILE_READING:
                read_file()
            case MenuOption.WEBPAGE_READING:
                read_webpage()
            case _: # handle all other cases
                print("Invalid option")


if __name__ == "__main__":
    main()
