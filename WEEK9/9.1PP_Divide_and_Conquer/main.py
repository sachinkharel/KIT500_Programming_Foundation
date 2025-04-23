"""
main function for words_count program that counts 
the number of words, sentences, and average word length
from the user input text
"""

__author__ = "Sachin Kharel"

from words_count import  display_menu, split_paragraph, user_input, words_list

def main():
    """
    Main function to run the words_count program.
    It prompts the user for text input and displays the analysis results.
    """
    
    # Display program's name
    print("\n Welcome to Words Count Program \n")
    
    # Prompt the user for text input
    paragraph:str = user_input()
    
    # split the paragraph into sentences
    sentences:list[str] = split_paragraph(paragraph)
    
    # split the sentences into words
    words:list[str] = words_list(sentences)
    
    #display menu
    display_menu(sentences, words)


if __name__ == "__main__":
    main()
    
    
    
    