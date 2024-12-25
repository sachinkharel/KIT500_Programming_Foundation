"""
Program to find common names from a list using dictionary.
"""

__author__ = "Sachin Kharel"

def main():
    namesfile = open("Practice/findcommon.txt")
    wordlist = list()
    tempword = str()
    for word in namesfile:
        tempword = tempword + (word.strip())
    wordlist = tempword.split()
    namedict = dict()
    maxvalue = 0
    maxkey = str()
    # namelist = ['sachin', 'suman', 'sachin', 'subash', 'sachin', 'suman', 'suman', 'sachin']
    for name in wordlist:
        # if name not in namedict:
        #     namedict[name] = 1
        #     print(name)
        # else:
        #     namedict[name] = namedict[name] + 1
        namedict[name] = namedict.get(name,0) + 1   #using idiom to count the names
        if maxvalue < namedict[name]:
            maxvalue = namedict[name]
            maxkey = name
    print(maxkey, maxvalue)
    


if __name__ == "__main__":
    main()