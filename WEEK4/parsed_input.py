"""
4.3CR User Input Functions
"""

__author__ = "Sachin Kharel"


def input_int(prompt:str, lower:int, upper:int) -> int:
    """
    This function takes in a prompt, a lower value and a upper value and returns the valid value entered by the user
    """
    #Prompt the user for an integer and take the input
    value:int = int(input(prompt)) #Convert the input to an integer
    
    #If the integer is not between low and high, print an error message and ask again
    while (value<lower or value>upper):
        print("Invalid input. Please try again.")
        value = int(input(prompt))
    #Return the integer
    return value
    


def input_float(prompt:str, lower:float, upper:float) -> float:
    """
    This function takes in a prompt, a lower value and a upper value and returns the valid value entered by the user
    """
    #Prompt the user for a float and take the input
    value:float = float(input(prompt)) #Convert the input to a float
    
    #If the float is not between low and high, print an error message and ask again
    while (value<lower or value>upper):
        print("Invalid input. Please try again.")
        value = float(input(prompt))
    #Return the float
    return value


def input_bool( prompt:str) -> bool:
    """
    This function takes in a prompt and returns the valid value entered by the user
    """
    #Prompt the user for a boolean and take the input
    value:str = input(f"{prompt} (yes/no)").lower() #Convert the input to lowercase
    
    #If the input is not yes or no, print an error message and ask again
    while value not in ["yes","no", "y", "n", "true", "false"]:
        print("Invalid input. Please try again.")
        value = input("(yes/no)").lower()
    #Return the boolean
    if value == "yes" or value == "y" or value == "true":
        return True
    else:
        return False


if __name__ == "__main__":
    #All variables are initialised so code will run without error before all functions are implemented and called
    stars = -1     #user's star (between 0 and 5)
    volume = -1.0  #continuously variable speaker volume (as a value between 0 and 11)
    again = False  #do they want to try some action again?

    print("Testing input_int... the number should be saved in stars.")
    print(" - Enter '6' (should loop with error)")
    print(" - Enter '-1' (should loop with error")
    print(" - Enter '2' and it should work")
    stars = input_int("Rate the last movie you saw", 0, 5)
    print(f"Star rating: {stars}");
    print()

    print("Testing input_float... the number should be saved in volume.")
    print(" - Enter '20' (should loop with error)")
    print(" - Enter '-1' (should loop with error)")
    print(" - Enter '9.5' and it should work")
    volume = input_float("Enter amplifier volume", 0.0, 11.0)
    print(f"Volume: {volume}")
    print()

    print("Testing input_bool... the result is saved in again.")
    print(" - Extend these boolean tests by adding more messages to verify your solution!")
    print(" - Enter 'nah' and it should loop with error")
    print(" - Enter 'yes' and it should succeed")
    again = input_bool("Try again?")
    print(f"Again: {again}")
    print()
    print(" - Verify that it can also read in False...")
    again = input_bool("Try again?")
    print(f"Again: {again}")
    print()

    print("Tests complete...")
