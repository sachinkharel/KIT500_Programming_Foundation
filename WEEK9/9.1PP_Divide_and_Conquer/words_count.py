"""
Group of functions to perform text analysis on a paragraph.
It includes functions to get user input, split the paragraph into sentences,
count sentences and words, calculate average word length, and display results.
"""

__author__ = "Sachin Kharel"

from calendar import c


def user_input() -> str:
    """
    Function to get user input for text analysis.
    It prompts the user for a paragraph of text and returns it.
    """
    
    # Prompt the user for a paragraph of text
    text = str(input("Enter a paragraph of text: "))
    if text[-1:] == ".":
        # Remove the last character if it's a period(.)
        # print("Last character is a period")
        text = text[:-1]
    return text

def split_paragraph(paragraph: str) -> list:
    """
    Function to split the paragraph into sentences.
    It returns a list of sentences.
    """
    
    # Split the paragraph into sentences using '.' as a delimiter
    sentences: list[str] = paragraph.split('.')
    # print(sentences)
    
    return sentences

def sentences_count(sentences: list[str]) -> int:
    """
    Function to count the number of sentences in the list.
    It returns the count of sentences.
    """
    
    # Count the number of sentences in the list
    sentence_count = len(sentences)
    
    return sentence_count

def words_list(sentences: list[str]) -> list[str]:
    """
    Function to split each sentence into words.
    It returns a list of words.
    """
    
    # Split each sentence into words and return the list
    word_list: list[str] = []
    for sentence in sentences:
        words = sentence.split()
        word_list.extend(words)
    
    return word_list

def words_count(words_list: list[str]) -> int:
    """
    Function to count the number of words in the list.
    It returns the count of words.
    """
    
    # Count the number of words in the list
    word_count = len(words_list)
    
    return word_count

def average_word_length(words_list: list[str]) -> float:
    """
    Function to calculate the average word length.
    It returns the average word length.
    """
    
    # Calculate the average word length
    total_length = 0
    
    for word in words_list:
        total_length += len(word)
    
    avg_length = total_length / len(words_list)
    
    return avg_length
    
def display_paragraph(sentences: list[str]):
    """
    Function to display the paragraph.
    It takes a list of sentences and prints them.
    """
    
    for sentence in sentences:
        print(sentence + ".")

def full_report(sentences: list[str], words_list: list[str]):
    """
    Function to display the full report of the text analysis.
    It takes a list of sentences and a list of words and prints the report.
    """
    
    print("Sentences:", sentences_count(sentences))
    print("Word count:", words_count(words_list))
    print("Average word length:", f"{average_word_length(words_list):1f}")
    

def display_menu( sentences: list[str], words_list: list[str]):
    """
    Function to display the menu options for the user.
    It returns the user's choice.
    """
    choice: str = ""  # the user's menu selection, initialised to an empty str
    
    while choice !="6" :
        
        print("\n1. Display paragraph")
        print("2. Count sentences")
        print("3. Count words")
        print("4. Average word length")
        print("5. Full report")
        print("6. Exit \n")
    
        choice = str(input("\nEnter your choice: "))
        
        if choice == "1":
            display_paragraph(sentences) # display the paragraph
        elif choice == "2":
            print("Sentences:", sentences_count(sentences)) # count the sentences
        elif choice == "3":
            print("Word count:", words_count(words_list)) # count the words
        elif choice == "4":
            print("Average word length:", f"{average_word_length(words_list):.1f}") #calculate the average word length
        elif choice == "5":
            full_report(sentences, words_list)  # display the full report
        else:
            print("Invalid choice. Please try again.")
    
          
        
        
    
    
    