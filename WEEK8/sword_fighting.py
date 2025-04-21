"""
Insult Sword Fighting Simulator
(inspired by LucasArts' The Secret of Monkey Island)
"""

__author__ = "Anonymous, Sachin Kharel"

import random
import time
from typing import Optional
from util import sequence, random_sequence


# Not an error. Intended to be const; should not be modified by the code.
INSULTS: list[str] = [
    "You're like a treasure map with all the X's missing.",
    "I've seen seaweed with more backbone.",
    "I've met rocks with more charisma than you.",
    "You fight like a dairy farmer",
    "Your breath could knock out a kraken",
    "You're about as threatening as a damp sponge."
]

# Not an error. Intended to be const; should not be modified by the code.
COMEBACKS: list[str] = [
    "And yet I still lead to more gold than you’ll ever see.",
    "Then you must stare at your reflection a lot.",
    "Too bad you’re not half as solid.",
    "How appropriate. You fight like a cow",
    "At least it’s effective at clearing out scum like you.",
    "Funny—this sponge just soaked up your pride."
]

# Not an error. Intended to be const; should not be modified by the code.
PLAYER: str = "Will Turner"
PIRATE: str = "Jack Sparrow"
ROUNDS_PER_GAME: int = 6


def print_n_pause(message: str, seconds: float):
    print(message)
    time.sleep(seconds)


def display_title():
    print_n_pause("Somewhere in the Devil's Triangle...\n\n\n", 1.5)
    print_n_pause("      THE SECRET OF THE", 1)
    print_n_pause("   FLYING DUTCHMAN", 2)
    print(f"\nYour name is {PLAYER} and you want to learn the pirate art of sword fighting!\n")
    _enter = input("Lets start your training, press enter to begin ")


def display_position(pos: int, rounds: int):
    print("LOSE ", end="")
    for i in range(0, rounds+1):
        print("|" if i == pos else "-", end="")
    print(" WIN")


def display_random_menu(options: list[str]) -> int:
    selection: int = -1
    seq: list[int] = random_sequence(len(options))

    for i, s in enumerate(seq):
        print(f"{i+1}. {options[s]}")

    while selection < 1 or selection > len(options):
        response = input("Select your comeback: ")
        if response.isdigit():
            selection = int(response)

    return seq[selection-1]


def speak(who: str, what: str):
    print_n_pause(f"\n{who}: {what}", 0.5)


def attack_parry() -> int:
    VICTORY: int = 1
    DEFEAT: int = -1
    outcome: int
    insult: int = random.randint(0, len(INSULTS) - 1)
    comeback: int

    speak(PIRATE, INSULTS[insult])
    print()

    comeback = display_random_menu(COMEBACKS)
    speak(PLAYER, COMEBACKS[comeback])

    if comeback == insult:
        outcome = VICTORY
        print("You advance!")
    else:
        outcome = DEFEAT
        print("You are pushed back!")

    return outcome


def fight(rounds: int):
    pos: int = rounds // 2

    display_position(pos, rounds)
    while pos > 0 and pos < rounds:
        pos -= attack_parry()
        display_position(pos, rounds)

    if pos == rounds:
        speak(PIRATE, "Arrrr! You've beaten me!")
    else:
        speak(PLAYER, "I give up! You win!")


def play_again() -> bool:
    again: Optional[bool] = None
    while again is None:
        response = input("Play again? (y)arr/(n)arr: ")
        match response:
            case "y" | "yarr":
                again = True
            case "n" | "narr":
                again = False
    return again


def loading():
    print("LOADING", end="")
    for i in range(10):
        print(".", end="", flush=True)
        time.sleep(random.random())
    print("DONE")
    print()


def start_playing():
    keep_playing: bool = True

    loading()
    display_title()
    while keep_playing:
        fight(ROUNDS_PER_GAME)
        keep_playing = play_again()


def main():
    start_playing()


if __name__ == "__main__":
    main()