"""
3.2PP Champions Trophy 2025 - Semi-Finalists
Program to take user input to display a formatted summary of the top four semi-finalists 
and how thrilled their home cities are about their success.
"""

__author__ = "Sachin Kharel"


def main():

    team_1: str = input("Enter the name of the first semi-finalist team: ")
    city_1: str = input(f"Enter the name of a major city from {team_1}: ")
    points_1: int = int(input(f"How many points did {team_1} earn in the group stage? "))
    team_2: str = input("Enter the name of the second semi-finalist team: ")
    city_2: str = input(f"Enter the name of a major city from {team_2}: ")
    points_2: int = int(input(f"How many points did {team_2} earn in the group stage? "))
    team_3: str = input("Enter the name of the third semi-finalist team: ")
    city_3: str = input(f"Enter the name of a major city from {team_3}: ")
    points_3: int = int(input(f"How many points did {team_3} earn in the group stage? "))
    team_4: str = input("Enter the name of the fourth semi-finalist team: ")
    city_4: str = input(f"Enter the name of a major city from {team_4}: ")
    points_4: int = int(input(f"How many points did {team_4} earn in the group stage? "))
    
    print()
    print("Champions Trophy 2025 - Semi-Finalists")
    print()


    print("The semi-finalists have been decided!")
    print()
    
    print(f"{team_1} has secured a spot with {points_1} points. Fans in {city_1} are overjoyed!")
    print(f"{team_2} follows closely behind with {points_2} points. The streets of {city_2} are alive with celebration!")
    print(f"{team_3} advances to the semis with {points_3} points. Cricket fever is at its peak in {city_3}!")
    print(f"{team_4} makes it through with {points_4} points. Cheers echo across {city_4} as they celebrate their team’s success!")
    
    print()
    print("Who will lift the Champions Trophy? Stay tuned for the thrilling knockout matches ahead!")
    
if __name__ == "__main__":
    main()