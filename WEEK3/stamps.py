"""
KIT101 3.2PP Stamp Function

Implements a reusable 'stamp' that can draw the author's initials at
any location on the Turtle Graphics window taking the x and y co-ordinate with
the ink color as parameter input)
"""

__author__ = "Sachin Kharel"

from turtle import Turtle
import turtle 


def place_stamp(stamper: Turtle, x:float, y:float, ink:str): 
    """
    Draws the author's initials with the starting point (x,y) and the
    color (ink)
    """
    # saving turtle initial state with storing initial values in -
    # below variables
    
    old_ink:str = turtle.pencolor()         #get color from turtle of current state
    old_direction:float = turtle.heading()  #get angle from turtle of current state
    old_x: float = turtle.xcor()            #get x co-ordinate from turtle of current state
    old_y: float = turtle.ycor()            #get y co-ordinate from turtle of current state
    
    # go to the point taking the co-ordinates from parameter input(x,y)
    stamper.penup()
    stamper.goto(x+50,y)
    stamper.pendown()
    
    # set the pen color from the parameter input (ink)
    stamper.pencolor(ink)
    
    stamper.left(180)             #starts to create S
    stamper.forward(40)
    stamper.left(90)
    stamper.forward(40)
    stamper.left(90)
    stamper.forward(40)
    stamper.right(90)
    stamper.forward(40)
    stamper.right(90)
    stamper.forward(40)
    stamper.penup()               #end of S with moving pen up
    
    stamper.right(90)             #placing pointer to create K
    stamper.forward(80)
    stamper.right(90)
    stamper.forward(50)
    stamper.pendown()
    
    stamper.right(90)             #starts to create K
    stamper.forward(80)           #we've made a line for K
    
    stamper.penup()               #placing pointer to complete K
    stamper.left(180)             
    stamper.forward(40)
    stamper.pendown()
    
    stamper.right(45)             #completing the remaining K
    stamper.forward(55)
    stamper.penup()
    stamper.left(180)
    stamper.forward(55)
    stamper.pendown()
    stamper.left(90)
    stamper.forward(55)           #K completed
    
    stamper.teleport(old_x,old_y)   #teleport to the old point
    stamper.setheading(old_direction)   #set the old angle
    stamper.pencolor(old_ink)           #set the old pencolor
    

def main():
    t = Turtle() # The turtle graphics object

    #call place_stamp funtion to draw initials with the given parameter input.
    place_stamp(t,-100,30, "blue")
    place_stamp(t,0,6, "green")

    # Avoid closing the window automatically
    t.screen.mainloop()


if __name__ == "__main__":
    main()
