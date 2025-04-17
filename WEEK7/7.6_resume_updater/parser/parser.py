from docx import Document



class ResumeParser:
    """
    A class to parse and structure a resume from a .docx file.
    
    This class will extract all relevant sections of a resume like Education, Experience,
    Skills, Leadership, Activities, and Projects.
    """
    
    def __init__(self, file_path):
        """
        Initializes the ResumeParser with the path to the .docx file.
        
        Args:
            file_path (str): The path to the .docx file containing the resume.
        """
        self.file_path = file_path
        
        self.doc = Document(file_path) #open the docx file using the docx library
        
        # Initialise empty directionaries to store parsed sections
        self.sections = {
            "Education": [],
            "Experience": [],
            'Skills & Interests': [],
            'Leadership & Activities': [],
            'Projects': []
        }
    
    def parse(self):
        """
        Parse the resume sections from the provided .docx file.

        This method processes the content of the .docx file and organizes it into different
        sections: Education, Experience, Skills & Interests, Leadership & Activities, and Projects.
        It assumes that these sections are clearly marked in the document.
        """
        
        # Iterate through each paragraph in the document
        current_section = None  # A variable to track which section we're currently parsing
        
        for section in self.doc.paragraphs:
            #Clean up the text by stripping unnecessary spaces or special characters
            text = section.text.strip()
            
            #check if the paragraph text corresponds to a section header
            if text == "Education":
                current_section = "Education"
            elif text == "Experience":
                current_section = "Experience"
            elif text == "Skills & Interests":
                current_section = "Skills & Interests"
            elif text == "Leadership & Activities":
                current_section = "Leadership & Activities"
            elif text == "Projects":
                current_section = "Projects"
            
            # If we are in a section, add the text to the corresponding list
            elif current_section and text:
                # Append the text to the current section's list
                self.sections[current_section].append(text)
        
        #After parsing, we can print the sections to verify the content
        self.print_sections()
    
    def print_sections(self):
        """
        Print the parsed sections of the resume to the console.
        
        This method iterates through the parsed sections and prints each section's title
        followed by its content.
        """
        for section, content in self.sections.items():
            print(f"{section}:")
            for item in content:
                print(f" - {item}")
            print()

def main():
    """
    Main function to initialize the parser and start the parsing process.
    It assumes the resume file path is provided.
    """
    
    # Specify the path to the resume file
    resume_file = "/Users/sachinutas/Downloads/Sachin Kharel Resume.docx"
    # Initialize the ResumeParser with the provided resume file
    parser = ResumeParser(resume_file)
    
    # Parse the content of the resume
    parser.parse()
    
if __name__ == "__main__":
    # Run the main function when the script is executed
    main()