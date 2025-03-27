"""
Program to print Hello World / any other string 
"""

__author__ = "Sachin Kharel"

#def greet_users(greet: str):
#    "prints the string received by greet in a signle line"
#    print(greet)

def main():
    
    print(search_target([ 12, 45, 3, 18, 25], 18))

def search_target(data: list[int], target: int) -> bool: # Function to search for a target in a list.
    index = 0
    stopped = False

    while index < len(data) and not stopped:
        if data[index] == target:
            stopped = True
        index += 1

    return stopped

   
    

if __name__ == "__main__":
    main()