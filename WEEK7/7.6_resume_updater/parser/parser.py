from docx import Document
from models.enums import SectionType
from models.section_data import ResumeSection



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
        
        # Initialize a dictionary where each SectionType enum member maps to an empty list for storing resume content

        self.sections = {section: [] for section in SectionType}
        
    
    def parse(self) -> list[ResumeSection]:
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
            if text == SectionType.EDUCATION.value:
                current_section = SectionType.EDUCATION
            elif text == SectionType.EXPERIENCE.value:
                current_section = SectionType.EXPERIENCE
            elif text == SectionType.SKILLS_AND_INTERESTS.value:
                current_section = SectionType.SKILLS_AND_INTERESTS
            elif text == SectionType.LEADERSHIP_AND_ACTIVITIES.value:
                current_section = SectionType.LEADERSHIP_AND_ACTIVITIES
            elif text == SectionType.PROJECTS.value:
                current_section = SectionType.PROJECTS
            
            # If we are in a section and the text is not empty, append it to the current section
            elif current_section and text:
                
                # Create a new ResumeSection object for the current text
                resume_section = ResumeSection(section_type=current_section, content=text)
                
                # Append the ResumeSection object to the corresponding section list
                self.sections[current_section].append(resume_section)
        
        
        # #After parsing, we can print the sections to verify the content
        # self.print_sections()
        
        # Return the parsed sections as a list of ResumeSection objects
        parsed_sections = []
        for section_items in self.sections.values():
            parsed_sections.extend(section_items)
   
        return parsed_sections
    
    # def print_sections(self):
    #     """
    #     Print the parsed sections of the resume to the console.
        
    #     This method iterates through the parsed sections and prints each section's title
    #     followed by its content.
    #     """
    #     for section, content in self.sections.items():
    #         print(f"{section}:")
    #         for item in content:
    #             print(f" - {item}")
    #         print()

