"""
Making random squares using the random module and using turtle 
module to draw the square 
"""

__author__ = "Org: James Montgomery, Modified by: Sachin Kharel"

import turtle as t
import random as rand

def get_random(a:int , b:int) -> int:
    "returns a random integer between a to b"
    length = rand.randrange(a,b) 
    return length

def main():
    length = get_random(10,100)                #length of the square received from get_random function     
    t.hideturtle()
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.write(length)                         #to see what was the random length
    t.mainloop()


if __name__ == "__main__":
    main()