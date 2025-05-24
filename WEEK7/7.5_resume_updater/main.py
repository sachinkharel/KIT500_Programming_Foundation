import re
from parser import ResumeParser
from enums import FileType
from json_creator import save_dict_to_json
from git_utils import push_json_to_github
import os
import json


def main():
    """
    Main function to initialize the parser and start the parsing process.
    It asks for the path to the resume file and checks if the file is in the correct format.
    """
    
    print("Welcome to the Resume Updater!")
    
    
    # Prompt the user for the path to the resume file
    
    resume_file = input("Enter the full path to your resume file (e.g., /Users/sachinutas/Desktop/Sachin Kharel Resume.docx): ")

    print("Parsing your resume...")
    
    # Check if the file path is valid
    
    while not os.path.exists(resume_file):
        print("File not found. Please provide a valid file path.")
        resume_file = input("Enter the path to your resume file (e.g., resume.docx): ")
    
    # Check until user provides a valid file type
    
    while not resume_file.endswith(FileType.DOCX.value):
        print("Invalid file format. Please provide a .docx file.")
        resume_file = input("Enter the path to your resume file (e.g., resume.docx): ")

    try:
        # Initialize the ResumeParser with the provided resume file
        
        parser = ResumeParser(resume_file)
        
        # Parse the content of the resume
        
        parsed_sections = parser.parse()
    
    except Exception as e:
        print(f"Error parsing the resume: {e}")
        return
    
    # Prompt the user with a menu of options
    
    choice: int = -1 # Initialize choice to a default value
    
    while choice != 0:
        print()
        print("1. Preview of parsed resume\n"
              "2. Save parsed resume in my computer\n"
              "3. Push parsed resume to GitHub\n"
              "0. Quit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                # Preview the parsed resume
                print("Parsed Resume:")
                # Pretty print the parsed resume in JSON format
                print(json.dumps(parsed_sections, indent=4))
                
            case 2:
                # Save the parsed resume to a JSON file
                json_file = "resume.json"
                save_dict_to_json(parsed_sections, json_file)
                print(f"Parsed resume saved to {json_file}")
            case 3:
                # Save the parsed resume to a JSON file
                json_file = "resume.json"
                save_dict_to_json(parsed_sections, json_file)
                repo_name = str(input("Enter the GitHub username/repository (e.g., sachinkharel/PersonalWebsite): "))
                # Push the parsed resume to GitHub
                push_json_to_github(
                    repo_name= repo_name,
                    local_json_file="resume.json",
                    file_path_in_repo="/resume.json",
                    commit_message="update of resume.json"
                )
    
            case 0:
                print("Exiting the program....")
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()