"""
Program to count lines from a text file.
"""

__author__ = "Sachin Kharel"

def main():
    fhand = open("Practice/test.txt")
    count = 0
    for line in fhand:
        count =count + 1
        print(count, line)
    print("\nLine count: ", count)
    

if __name__ == "__main__":
    main()
