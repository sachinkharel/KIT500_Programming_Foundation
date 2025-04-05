"""
6.2CR Dictionaries
"""

__author__ = "Sachin Kharel"


from math import e
from operator import add
from turtle import st


def add_student(results: dict[str, list[int]], sid: str):
    """
    Adds a new student ID.
    """
    # Check if student already exists
    if sid in results:
        print(f"Student {sid} already exists.")
    else:
        results[sid] = []

def add_student_result(results: dict[str, list[int]], sid: str, result: int):
    """
    Adds a result to the results on record for an existing student.
    """
    # Check if student exists and result is valid
    if sid not in results:
        print(f"Student {sid} does not exist.")
    elif result < 0 or result > 100:
        print("Invalid result. Please enter a result between 0-100.")
    else:
        results[sid].append(result)


def calculate_average(results: dict[str, list[int]]) -> float:
    """
    Calculates the average result for all students.
    """
    total: int = 0 # total of all results
    count: int = 0 # number of results
    average: float = 0.0 # average result
    
    for value in results.values():
        total += sum(value) # sum of all results
        count += len(value) # number of results
    if count > 0:
        average = total / count
        
    else:
        print("No student results recorded.")
    
    return average

def calculate_cumulative_gpa(results: dict[str, list[int]], student_id: str) -> float:
    
    gpa_value: int              # value of gpa
    gpa: float = 0.0            # cumulative gpa
    student_results: list[int]  # results for a student
    
    if student_id in results:
        student_results = results[student_id]
        for result in student_results:
            gpa_value = 0
            if result >= 80:
                gpa_value = 7
            elif result >= 70:
                gpa_value = 6
            elif result >= 60:
                gpa_value = 5
            elif result >= 50:
                gpa_value = 4
            gpa += gpa_value * 12.5
        gpa = gpa / (len(student_results) * 12.5)
    else:
        print(f"No student with id {student_id} exists.")
    return gpa 
    


def list_students(results: dict[str, list[int]]):
    """
    Displays all students and their results.
    """
    print(f"Displaying students and results for {len(results)} record(s):")
    
    # Display results for each student
    for k, v in results.items():
        print(f"Results for {k}: {v}")


def main():
    results: dict[str, list[int]] = {} # collection of students and unit results
    sid: str # student ID
    res: int # result in the range 0-100
    choice: int = 0 # user's menu selection

    SID_PROMPT = "Enter the student ID: "                   # prompt for student ID
    RES_PROMPT = "Enter a unit result between 0-100: "      # prompt for unit result

    print("Student GPA Calculator")
    while choice != 6:
        print()
        print("1. Add student\n"
              "2. Add result to existing student\n"
              "3. Calculate average\n"
              "4. Calculate GPA\n"
              "5. List students\n"
              "6. Quit")
        choice = int(input("Action: "))
        match choice:
            case 1:
                sid = input(SID_PROMPT)                         # prompt for student ID
                add_student(results, sid)                       # add student to results
            case 2:
                sid = input(SID_PROMPT)                         # prompt for student ID
                res = int(input(RES_PROMPT))                    # prompt for unit result    
                add_student_result(results, sid, res)           # add result to student
            case 3:
                average = calculate_average(results)            # calculate average result
                print(f"Cohort average is {average:.1f}")       # display average result
                
            case 4:
                sid = input(SID_PROMPT)                         # prompt for student ID  
                gpa = calculate_cumulative_gpa(results, sid)    # calculate GPA       
                print(f"Cumulative GPA for student {sid} is {gpa:.1f}") # display GPA
            case 5:
                list_students(results)                          # list all students and results


if __name__ == "__main__":
    main()
