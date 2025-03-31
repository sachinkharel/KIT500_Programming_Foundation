"""
5.2PP Collection of Strings
"""

__author__ = "Sachin Kharel"


def add_word(word_list: list[str], word: str):
    """
    Adds a new word to the word list if there is capacity and
    the word is not empty.
    """
    if word in word_list:
         print("Word already exists.")
    elif word == "":
        print("Word cannot be empty.")
    else:
       word_list.append(word)


def display_entries(word_list: list[str]):
    """
    Displays all words in the word list, separated by a comma.
    """
    final_string: str = ""
    if len(word_list) == 0:
        print("No words to display.")
    for word in word_list:
        final_string += word + ", "
       
    print(final_string[:-2]) #to remove the last comma and space

def average_len(word_list: list[str]) -> float:
    """
    Calculate the sum of each word's length
    Calculate and return the average word length (that sum divided by len(word_list))
    """
    if len(word_list) == 0:
        print("No words in the list.")
        return 0
    
    total_len: int = 0      #total length of all words
    average: float = 0.0    #average length of all words
    for i in word_list:
        total_len += len(i)
    average = total_len / len(word_list)
    
    return average

def main():
    """
    Display a menu and respond to user choices to add words, display entries
    and display the average word length.
    """
    
    words: list[str] = []   #collection of words, initialised to an empty list
    choice: str = ""        #the user's menu selection, initialised to an empty str
    new_word:str            #new word given by the user
    
    print("Words!")
    
    
    while choice != "4":
        print()
        print("1. Add a word")
        print("2. Display entries")
        print("3. Display average word length")
        print("4. Quit\n")
        choice = (input("Enter your choice: \n"))
        if choice == "1":
            print("Choice 1 selected\n")
            new_word = input("Enter a word: ")
            add_word(words, new_word)
        elif choice == "2":
            print("Choice 2 selected\n")
            display_entries(words)
        elif choice == "3":
            print("Choice 3 selected\n")
            print("Average word length: ", average_len(words))
        elif choice == "4":
            print("Choice 4 selected, Game ended")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
