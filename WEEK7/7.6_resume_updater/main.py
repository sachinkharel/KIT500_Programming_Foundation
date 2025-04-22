from parser.parser import ResumeParser
from models.enums import FileType


def main():
    """
    Main function to initialize the parser and start the parsing process.
    It asks for the path to the resume file and checks if the file is in the correct format.
    """
    
    # Prompt the user for the path to the resume file
    
    resume_file = input("Enter the path to your resume file (e.g., resume.docx): ")
    
    # Check until user provides a valid file path
    
    while not resume_file.endswith(FileType.DOCX.value):
        print("Invalid file format. Please provide a .docx file.")
        resume_file = input("Enter the path to your resume file (e.g., resume.docx): ")

    
    # Initialize the ResumeParser with the provided resume file
    parser = ResumeParser(resume_file)
    
    # Parse the content of the resume
    parsed_sections = parser.parse()
    
    # Print to see the parsed output
    for section in parsed_sections:
        print(f"{section.section_type.value}: {section.content}")
    
if __name__ == "__main__":
    # Run the main function when the script is executed
    main()