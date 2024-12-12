"""
Drawing the initial of my Name using turtle graphics module"
"""

__author__ = "Org: James Montgomery, Modified by: Sachin Kharel"

import turtle as t

def main():
    
    t.hideturtle() 
    t.left(180)             #starts to create S
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.penup()               #end of S with moving pen up
    
    t.right(90)             #placing pointer to create K
    t.forward(80)
    t.right(90)
    t.forward(50)
    t.pendown()
    
    t.right(90)             #starts to create K
    t.forward(80)           #we've made a line for K
    
    t.penup()               #placing pointer to complete K
    t.left(180)             
    t.forward(40)
    t.pendown()
    
    t.right(45)             #completing the remaining K
    t.forward(55)
    t.penup()
    t.left(180)
    t.forward(55)
    t.pendown()
    t.left(90)
    t.forward(55)           #K completed
    
    t.mainloop()            
    


if __name__ == "__main__":
    main()