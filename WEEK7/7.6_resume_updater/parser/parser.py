import re
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
        
        self.doc = Document(file_path)  # open the docx file using the docx library
        
        # Initialize a dictionary where each SectionType enum member maps to an empty list for storing resume content
        self.sections = {section: [] for section in SectionType}
        
    def parse(self) -> dict:
        """
        Parse the resume sections from the provided .docx file.

        This method processes the content of the .docx file and organizes it into different
        sections: Education, Experience, Skills & Interests, Leadership & Activities, and Projects.
        It assumes that these sections are clearly marked in the document.
        """
        
        # Iterate through each paragraph in the document
        current_section = None  # A variable to track which section we're currently parsing
        current_data = {}
        
        for section in self.doc.paragraphs:
            # Clean up the text by stripping unnecessary spaces or special characters
            text = section.text.strip()
            # print(f"Processing paragraph: {text}")  # Debugging output
            
            # Check if the paragraph text corresponds to a section header
            if text == SectionType.EDUCATION.value:
                current_section = SectionType.EDUCATION
                current_data["Education"] = []  # Initialize list for Education
            elif text == SectionType.EXPERIENCE.value:
                current_section = SectionType.EXPERIENCE
                current_data["Experience"] = []  # Initialize list for Experience
            elif text == SectionType.SKILLS_AND_INTERESTS.value:
                current_section = SectionType.SKILLS_AND_INTERESTS
                current_data["Skills & Interests"] = {"technical": [], "languages": [], "interests": []}  # Initialize nested dict
            elif text == SectionType.LEADERSHIP_AND_ACTIVITIES.value:
                current_section = SectionType.LEADERSHIP_AND_ACTIVITIES
                current_data["Leadership & Activities"] = []  # Initialize list for Leadership & Activities
            elif text == SectionType.PROJECTS.value:
                current_section = SectionType.PROJECTS
                current_data["Projects"] = []  # Initialize list for Projects

                
            
            # If we are in a section and the text is not empty, process the data
            elif current_section and text:
                # print(f"Current section: {current_section}")  # Debugging output
                if current_section == SectionType.EDUCATION:
                    # Process education data
                    data = self.parse_education_data(section)
                    # print(f"Parsed education data: {data}")  # Debugging output
                    if data:
                        current_data["Education"].append(data)
                elif current_section == SectionType.EXPERIENCE:
                    # Process experience data
                    data = self.parse_experience_data(section)
                    if data:
                        current_data["Experience"].append(data)
                elif current_section == SectionType.SKILLS_AND_INTERESTS:
                    # Process skills data
                    data = self.parse_skills_data(section)
                    if data:
                        current_data["Skills & Interests"].update(data)
                elif current_section == SectionType.LEADERSHIP_AND_ACTIVITIES:
                    # Process leadership data
                    data = self.parse_leadership_data(section)
                    if data:
                        current_data["Leadership & Activities"].append(data)
                elif current_section == SectionType.PROJECTS:
                    # Process project data
                    data = self.parse_projects_data(section)
                    if data:
                        current_data["Projects"].append(data)
        
        return current_data
    
    def extract_hyperlink(self, paragraph):
        """
        Extracts the first hyperlink (if any) from the given paragraph using XML relationships.
        """
        
        for rel in paragraph.part.rels.values():
            if rel.reltype == 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink':
                if rel.rId in paragraph._p.xml:
                    print(f"Found hyperlink: {rel.target_ref}")  # Debugging output
                    return rel.target_ref  # Corrected from .target to .target_ref
        return ""


    
    def parse_education_data(self, paragraph):
        """
        Parses education-related information from the provided text.
        This can be customized as per the document layout.
        """
        # Clean up the text to handle tabs or multiple spaces
        text = paragraph.text.replace("\t", " | ")  # Replace any tabs with a pipe to standardize
        
        # print(f"Parsing education data: {text}")  # Debugging output
        
        # Split the text into parts by '|'
        parts = [part.strip() for part in text.split(" | ") if part.strip()]    # Clean up empty parts so that we can get the right length and index
        
        # print(f"Split parts: {parts}")  # Debugging output
        
        link = self.extract_hyperlink(paragraph)
        
        
        if len(parts) >= 4:  # We expect at least 4 parts: institution, degree, location, duration
            # Return the parsed data in a dictionary format
            return {
                "institution": parts[0],  # Institution
                "degree": parts[1],       # Degree
                "location": parts[2],     # Location
                "duration": parts[3],     # Duration
                "gpa": parts[4] if len(parts) > 4 else "",  # Optional GPA
                "link": link  # You can handle links separately if required
            }
        return None

    
    def parse_experience_data(self, paragraph):
        """
        Parses experience-related information from the provided text.
        This can be customized as per the document layout.
        """

        # Format: Company | Role | Location | Duration
        text = paragraph.text.replace("\t", " | ")  # Replace any tabs with a pipe to standardize
        
        parts = [part.strip() for part in text.split(" | ") if part.strip()]    # Clean up empty parts so that we can get the right length and index
        # print(f"Parsing experience data: {text}")  # Debugging output
        # print(f"Split parts: {parts}")  # Debugging output

        link = self.extract_hyperlink(paragraph)

        
        if len(parts) >= 4:
            self.current_experience_entry = {
                "title": parts[0].strip(),
                "company": parts[1].strip(),
                "location": parts[2].strip(),
                "duration": parts[3].strip(),
                "description": [],  # We'll append descriptions
                "link": link  # Handle link extraction if any
            }
            return self.current_experience_entry
        
        # If it's a description line and a current entry exists, append the description
        if len(parts) == 1 and hasattr(self, 'current_experience_entry'):
            self.current_experience_entry["description"].append(parts[0].strip())
            return None    
        
        return None

    def parse_skills_data(self, paragraph):
        """
        Parses skills & interests-related information from the provided text.
        """
        # Assuming skills are listed by category: technical, languages, and interests
        categories = paragraph.text.split(" || ")
        data = {}
        if "Technical:" in categories[0]:
            data["technical"] = categories[0][10:].split(",")  # Remove "Technical:" and split skills
        if "Language:" in categories[1]:
            data["languages"] = categories[1][10:].split(",")  # Similar for languages
        if "Interests:" in categories[2]:
            data["interests"] = categories[2][10:].split(",")  # And for interests
        return data

    def parse_leadership_data(self, paragraph):
        """
        Parses leadership and activities-related information from the provided text.
        """
        text = paragraph.text.replace("\t", " | ")  # Replace any tabs with a pipe to standardize
        # print(f"Parsing leadership data: {text}")
        
        parts = [part.strip() for part in text.split(" | ") if part.strip()]    # Clean up empty parts so that we can get the right length and index

        
        link = self.extract_hyperlink(paragraph)
        
        
        # Check if the text contains a title and other structured data
        if len(parts) >= 4:
            # Create a new entry for the title and other details
            self.current_leadership_entry = {
                "title": parts[0].strip(),
                "organization": parts[1].strip(),
                "location": parts[2].strip(),
                "duration": parts[3].strip(),
                "description": [],  # Initialize an empty list for descriptions
                "link": link  # Handle link extraction if any
            }
            return self.current_leadership_entry
        
        # If it's a description line and a current entry exists, append the description
        if len(parts) == 1 and hasattr(self, 'current_leadership_entry'):
            self.current_leadership_entry["description"].append(parts[0].strip())
            return None
        
        return None

    def parse_projects_data(self, paragraph):
        """
        Parses project-related information from the provided text.
        """
        text = paragraph.text.replace("\t", " | ")  # Replace any tabs with a pipe to standardize
        # print(f"Parsing project data: {text}")
        # Format: Title | Duration
        parts = [part.strip() for part in text.split(" | ") if part.strip()]    # Clean up empty parts so that we can get the right length and index
        
        link = self.extract_hyperlink(paragraph)
        
        # print(f"Split parts: {parts}")
        if len(parts) >= 2:
            # Initialize a new project entry
            self.current_project_entry = {
                "title": parts[0].strip(),
                "duration": parts[1].strip(),
                "description": [],  # Add project descriptions
                "link": link  # Handle link if available
            }
            return self.current_project_entry
        # If it's a description line and a current entry exists, append the description
        if len(parts) == 1 and hasattr(self, 'current_project_entry'):
            self.current_project_entry["description"].append(parts[0].strip())
            return None
        
        return None
