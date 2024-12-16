"""
Program to find common names from a list using dictionary.
"""

__author__ = "Sachin Kharel"

def main():
    namedict = dict()
    listdict = ['sachin', 'suman', 'sachin', 'subash', 'sachin', 'suman', 'suman', 'sachin']
    for name in listdict:
        if name not in namedict:
            namedict[name] = 1
        else:
            namedict[name] = namedict[name] + 1
    print(namedict)


if __name__ == "__main__":
    main()