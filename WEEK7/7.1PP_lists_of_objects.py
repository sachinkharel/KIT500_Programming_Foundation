
"""
6.1PP Data Classes 
"""

__author__ = "Sachin Kharel"

from dataclasses import dataclass
from enum import Enum
from os import close


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
    
def add_many(tasks: list[Task], number_of_entries: int):
    """
    user to enter multiple records into the list(one at a time)
    """
    for i in range(number_of_entries):
        add_task(tasks)  # Use add_task function to collect and add one task at a time



def display_all(entries: list[Task]):
    """
    display all the records in the list
    """
    for line in entries:
        print(line)
        

# Function to add a single task to the list
def add_task(tasks: list[Task]):
    """
    Adds a new task to the tasks list by calling input_task.
    """
    task = create_task()  # Collect task details from the user
    tasks.append(task)  # Append the newly created Task object to the tasks list
    
    
# Function to find the most complete task in a specific category
def most_complete(tasks: list[Task], category: Category) -> Task | None:
    """
    Finds the most complete task in the specified category.
    """
    closest_task = None  # Initialize the closest task variable
    
    for task in tasks:
        if task.category == category:
            if closest_task is None or task.percent > closest_task.percent:
                closest_task = task
    
    return closest_task  # Return the most complete task in the specified category

# Function to get average completion percentage of tasks in a specific category
def average_completion(tasks: list[Task], category: Category) -> float:
    """
    Calculates the average completion percentage of tasks in the specified category.
    """
    total_percent = 0   # Initialize total percentage variable
    count = 0           # Initialize count variable    
    
    for task in tasks:  # Iterate through the tasks
        if task.category == category:
            total_percent += task.percent
            count += 1
            
    if count> 0:
        return total_percent / count # Return the average completion percentage
    else:
        return 0

def main():
    
    tasks = []  # Start with an empty list of tasks
    
    # Ask the user how many tasks they want to add initially
    num_of_entries = int(input("Enter the number of tasks you want to add: "))

    # Add the specified number of tasks in bulk
    add_many(tasks, num_of_entries)
    
    
    # Menu loop to interact with the user
    choice = None
    while choice != "4":
        print("\nMenu:")
        print("1. Add another task")
        print("2. Display all tasks, one per line")
        print("3. Find the most complete task in a category")
        print("4. Find the average completion percentage in a category")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)  # Calls add_task to add a single task
        elif choice == "2":
            display_all(tasks)  # Calls display_all to show all tasks
        elif choice == "3":
            print("Select category to find the most complete task:")
            category = category_name()
            task = most_complete(tasks, category) # Calls most_complete to find the most complete task
            if task:
                print(f"{task}")
            else:
                print(f"No tasks in {category.value} category.")        
        elif choice == "4":
            print("Select category to find the average completion percentage:")
            category = category_name()
            avg = average_completion(tasks, category)   # Calls average_completion to find the average completion percentage
            print(f"Average completion percentage for {category.value} category: {avg:.2f}%")
        elif choice == "5":
            print("Exiting the program.")
        else:
            print("Invalid choice. Please try again.")
    
    
if __name__ == "__main__":
    main()