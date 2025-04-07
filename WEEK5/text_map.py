"""
5.4DN Text Map
A command-driven program for working with grid-based maps rendered as text.
"""

import numpy as np

__author__ = "Sachin Kharel"


def create_map(string: str) -> np.ndarray:
    """
    Converts the multi-line string into a 2D array of single-letter strs.
    Each line in the str should be the same length for best results.
    """
    rows = string.splitlines()
    map = np.empty((len(rows), len(rows[0])), dtype=str)

    if len(rows) > 0:
        for i, line in enumerate(rows):
            map[i] = list(line)

    return map


def display_bordered_title(title: str):
    """
    Presents the given title text with a border of equals signs.
    """
    BORDER = "=" * (len(title) + 4)
    print(BORDER)
    print(f"= {title} =")
    print(BORDER)
    print()


def display_help():
    """
    Displays a list of available program commands.
    """
    print("Commands:\n"
          "?                \tShow this list of commands\n"
          "d                \tDisplay the map\n"
          "z row col        \tShow grid squares surrounding (row, col) \n"
          "r row col colour \tReplace region with colour (a single character) starting ar (row, col) \n"
          "l filename       \tLoad the text map from filename \n"
          "s filename       \tSave the current map to filename \n"
          "q                \tExit the program \n"
          "\nCommands may be chained together, separated by whitespace.")


def display_map(map: np.ndarray):
    """
    Displays the given character-based map with a leading and trailing blank line.
    """
    print("\n") # Leading blank line
    for row in map: 
        for element in row:
            print(f"{element} ", end="")
        print() # New line after each row
    print() # Trailing blank line
  



def is_inside(map: np.ndarray, row: int, col: int) -> bool:
    """
    Returns True if (row, col) is inside the map's bounds; False otherwise.
    """
    if  0 <= row < map.shape[0] and 0 <= col < map.shape[1]: # Check if row and col are within the bounds of the map
        return True
    return False


def zoom(map: np.ndarray, row: int, col: int):
    """
    Displays the 9 grid squares in the map centred at (row, col).
    Displays a space for any grid square that are outside the map's bounds.
    """
    for r in range(row - 1, row + 2):  # Loop through rows: row-1 to row+1
            for c in range(col - 1, col + 2):  # Loop through columns: col-1 to col+1
                if is_inside(map, r, c):  # Check if the cell is inside the map bounds
                    print(map[r, c], end="")  # Print the map character at this position
                else:
                    print(" ", end="")  # Print a space if the cell is out of bounds
            print()  # Move to the next line after printing the entire row
    

def replace(map: np.ndarray, row: int, col: int, with_colour: str) -> int:
    """
    Starts a flood fill operation by selecting the replacement grid square
    value at the given row and col. Returns the number of cells modified.
    """
    # Must be within the bounds of the map and not already equal to fill
    if is_inside(map, row, col) and  map[row, col] != with_colour:
        return flood_fill(map, row, col, map[row, col], with_colour)
    return 0


def flood_fill(map: np.ndarray, row: int, col: int, replace: str, with_colour: str) -> int:
    """
    Performs flood fill, replacing replace with with_colour,
    starting from (row, col) and returns the number of cells changed.
    """
    changed:int = 0 # Number of cells changed, initially 0
    if is_inside(map, row, col) and map[row, col] == replace:
        map[row, col] = with_colour # Replace the cell
        changed += 1 # Increment the count of changed cells
        
        # Recursively call flood_fill for the 4 adjacent cells
        changed += flood_fill(map, row - 1, col, replace, with_colour)
        changed += flood_fill(map, row + 1, col, replace, with_colour)
        changed += flood_fill(map, row, col - 1, replace, with_colour)
        changed += flood_fill(map, row, col + 1, replace, with_colour)
        return changed
    
    return 0


def main():
    map: np.ndarray # The character-based map
    command: list # User's entered command and parameters
    row: int # Command param for row
    col: int # Command param for col
    colour: str # Command param for colour

    # The initial map source.
    # Edited the initial map to contain spaces to create a lot of hollow spaces.
    # Be sure to keep the new line chars (\n) at the end of all but the last line
    str_map = ("####################\n"
               "######            ##\n"
               "######  ############\n"
               "######  ############\n"
               "######            ##\n"
               "################  ##\n"
               "################  ##\n"
               "######            ##\n"
               "####################")

    map = create_map(str_map)

    display_bordered_title("Text Map")
    command = input("Enter commands (? for help). "
                    "There are no further prompts after this point.\n").split()

    while command != ["q"]:
        match command:
            # TODO: Make required changes in the appropiate cases
            case ["d"]: # Display
                display_map(map)
            case ["z", row, col]: # Zoom
                zoom(map, int(row), int(col))
            case ["r", row, col, colour]: # Replace
                print(f"{replace(map, int(row), int(col), str(colour))} grid squares changed")
                
            case ["l"]: # Load
                print("Feature not implemented")
            case ["s"]: # Save
                print("Feature not implemented")
            case ["q"]: # Quit
                break
            case _:   # Unknown command. Will also capture ?
                display_help()

        # Wait for the next command
        command = input().split()


if __name__ == "__main__":
    main()
