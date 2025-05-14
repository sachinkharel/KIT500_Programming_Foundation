from parser import ResumeParser
from enums import FileType
from json_creator import save_dict_to_json
from git_utils import push_json_to_github
import os


def main():
    """
    Main function to initialize the parser and start the parsing process.
    It asks for the path to the resume file and checks if the file is in the correct format.
    """
    
    # Prompt the user for the path to the resume file
    
    resume_file = "/Users/sachinutas/Downloads/Sachin Kharel Resume.docx"
    
    #OR
    
    # resume_file = input("Enter the path to your resume file (e.g., resume.docx): ")
    
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
    
    json_file = "resume1.json"
    
    # Save the parsed sections to a JSON file
    
    save_dict_to_json(parsed_sections, json_file)
    
   
    # Push the JSON file to GitHub
    
    push_json_to_github(
        repo_name="sachinkharel/PersonalWebsite",
        local_json_file=json_file,
        file_path_in_repo="/resume.json",
        commit_message="update of resume.json"
    )

if __name__ == "__main__":
    main()