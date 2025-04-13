
"""
6.1PP Data Classes 
"""

__author__ = "Sachin Kharel"

from dataclasses import dataclass
from enum import Enum


#Define the enum 
class Category(Enum):
    """
    the enum class with its values
    """
    HOME = "Home"   #Home category
    WORK = "Work"   #Work category
    UNI = "Uni"     #University category

#Define the data class
@dataclass
class Task:
    
    """
    the data class fields with their types
    """
    
    description: str        #Description of the task
    percent: float          #Percentage of the task completed
    days_until_due: int     #Number of days until the task is due
    category: Category      #Category of the task
      

    #format the output
    def __str__(self) -> str:
        if self.percent <20:
            return f"{self.description} ({self.category.value}) - {self.days_until_due} days until due - {self.percent}% complete (Should work on this more)"
        elif self.percent >80:
            return f"{self.description} ({self.category.value}) - {self.days_until_due} days until due - {self.percent}% complete (Almost there!)"
        else:
            return f"{self.description} ({self.category.value}) - {self.days_until_due} days until due - {self.percent}% complete"

def category_name() -> Category:
    #Show a menu of human-readable versions of the enum's values
    #Have the user select one of them and return it
    i:int = 1
    for category in Category:
        print(f"{i} : {category.value}")
        i = i+1
    choice = input("Enter the category: ") #Read the user's choice
    
    #Validate the user's choice and return the corresponding enum value
    while choice not in ["1","2","3"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter the category: ")
    if choice == "1":
        choice = Category.HOME
    elif choice == "2":
        choice = Category.WORK
    else:
        choice = Category.UNI
    return choice

def create_task() -> Task:
    #Read and validate user input for values to store in the data class
    #Calls the category_name function to get that value
    #Creates and returns the newly created object
    
    task_d = input("Enter the task description: ")                              #Read the task description
    percent_d = float(input("Enter the percentage of the task completed: "))    #Read the percentage of the task completed
    days_d = int(input("Enter the number of days until the task is due: "))     #Read the number of days until the task is due
    category_d = category_name()                                              #Read the category of the task                
    
    return Task(task_d, percent_d, days_d, category_d)                          #Return the newly created object
    
    

def main():
    #Calls the function to read details from the user
    #and stores the result in data
    data: Task
    print("Enter task details")
    print()
    data = create_task() #Read the task details from the user

    #Displays the result calling print()
    print(data)
    
    
if __name__ == "__main__":
    main()