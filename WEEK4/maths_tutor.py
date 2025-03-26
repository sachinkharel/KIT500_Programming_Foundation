"""
4.1PP Selection and Repetition
"""

__author__ = "Sachin Kharel"

import random
import timeit  # Used for timing the execution of code
from random import randint  # Used for generating random values


def display_title(title: str):
    """
    Displays the given title in ALL CAPS, underlined by plus (+) symbols,
    and followed by a blank line.
    """
    print(title.upper())
    print(len(title)*"+")
    print()


def check_answer(num1: int, num2: int) -> bool:
    """
    Tests the user's ability to answer a given subtraction problem.
    Provides feedback and returns True if correct, False otherwise.
    """
    user_input: int  # The user's typed answer
    correct:bool = True # True if the user's answer is correct, False otherwise

    user_input = int(input(f"What is {num1} - {num2}? "))
    if user_input == num1 - num2:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {num1 - num2}")
        correct = False

    return correct

def start_quiz(max_value: int, target_correct: int) -> int:
    """
    Runs the math tutorial where the user must answer subtraction problems
    correctly until reaching the required number of correct answers.
    Returns the total number of attempts.
    """
    attempts:int = 0  # Total number of attempts
    correct_answers:int = 0 # Total number of correct answers
    a:int
    b:int
    
    while correct_answers < target_correct:
        a=randint(1,max_value)
        b=randint(1,max_value)
        attempts+=1
        if(check_answer(a,b)) is True:
            correct_answers+=1

    return attempts

def main():
    MAX_VALUE = 20  # Maximum operand value of random numbers
    REQUIRED_CORRECT = 5  # Number of correct answers required
    start_time: float  # Start time of quiz
    end_time: float  # End time of quiz
    total_attempts: int  # Total number of attempts made

    display_title("Math Quiz")
    print("Solve the subtraction problems as quickly as possible!")
    print(f"You must answer {REQUIRED_CORRECT} problems correctly to finish.")
    print(f"The numbers will be between 1 and {MAX_VALUE}.")
    print()

    # Start the quiz
    input("Press Enter to begin the timed test...")
    start_time = timeit.default_timer()
    total_attempts = start_quiz(MAX_VALUE, REQUIRED_CORRECT)
    end_time = timeit.default_timer()

    # Display performance results
    print()
    print("Total Attempts:", total_attempts)
    print(f"Accuracy: {(100 * REQUIRED_CORRECT / total_attempts):.1f}%")
    print(f"Total Time: {(end_time - start_time):.1f} seconds")
    print()
    display_title("Keep Practicing!")


if __name__ == "__main__":
    main()
