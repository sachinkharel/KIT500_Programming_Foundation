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
            print(f"Processing paragraph: {text}")  # Debugging output
            
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
                print(f"Current section: {current_section}")  # Debugging output
                if current_section == SectionType.EDUCATION:
                    # Process education data
                    data = self.parse_education_data(text)
                    print(f"Parsed education data: {data}")  # Debugging output
                    if data:
                        current_data["Education"].append(data)
                elif current_section == SectionType.EXPERIENCE:
                    # Process experience data
                    data = self.parse_experience_data(text)
                    if data:
                        current_data["Experience"].append(data)
                elif current_section == SectionType.SKILLS_AND_INTERESTS:
                    # Process skills data
                    data = self.parse_skills_data(text)
                    if data:
                        current_data["Skills & Interests"].update(data)
                elif current_section == SectionType.LEADERSHIP_AND_ACTIVITIES:
                    # Process leadership data
                    data = self.parse_leadership_data(text)
                    if data:
                        current_data["Leadership & Activities"].append(data)
                elif current_section == SectionType.PROJECTS:
                    # Process project data
                    data = self.parse_projects_data(text)
                    if data:
                        current_data["Projects"].append(data)
        
        return current_data
    
    def parse_education_data(self, text):
        """
        Parses education-related information from the provided text.
        This can be customized as per the document layout.
        """
        # Clean up the text to handle tabs or multiple spaces
        text = text.replace("\t", " | ")  # Replace any tabs with a pipe to standardize
        
        print(f"Parsing education data: {text}")  # Debugging output
        
        # Split the text into parts by '|'
        parts = [part.strip() for part in text.split("|")]
        
        print(f"Split parts: {parts}")  # Debugging output
        
        if len(parts) >= 4:  # We expect at least 4 parts: institution, degree, location, duration
            # Return the parsed data in a dictionary format
            return {
                "institution": parts[0],  # Institution
                "degree": parts[1],       # Degree
                "location": parts[2],     # Location
                "duration": parts[3],     # Duration
                "gpa": parts[4] if len(parts) > 4 else "",  # Optional GPA
                "link": ""  # You can handle links separately if required
            }
        return None

    
    def parse_experience_data(self, text):
        """
        Parses experience-related information from the provided text.
        This can be customized as per the document layout.
        """
        # Format: Company | Role | Location | Duration
        parts = text.split(" | ")
        if len(parts) >= 4:
            return {
                "title": parts[1].strip(),
                "company": parts[0].strip(),
                "location": parts[2].strip(),
                "duration": parts[3].strip(),
                "description": [],  # We'll append descriptions
                "link": ""  # Handle link extraction if any
            }
        return None

    def parse_skills_data(self, text):
        """
        Parses skills & interests-related information from the provided text.
        """
        # Assuming skills are listed by category: technical, languages, and interests
        categories = text.split(" || ")
        data = {}
        if "Technical:" in categories[0]:
            data["technical"] = categories[0][10:].split(",")  # Remove "Technical:" and split skills
        if "Language:" in categories[1]:
            data["languages"] = categories[1][10:].split(",")  # Similar for languages
        if "Interests:" in categories[2]:
            data["interests"] = categories[2][10:].split(",")  # And for interests
        return data

    def parse_leadership_data(self, text):
        """
        Parses leadership and activities-related information from the provided text.
        """
        text = text.replace("\t", " | ")  # Replace any tabs with a pipe to standardize
        print(f"Parsing leadership data: {text}")
        
        parts = text.split(" | ")
        print(f"Split parts: {parts}")
        if len(parts) >= 4:
            return {
                "title": parts[1].strip(),
                "organization": parts[0].strip(),
                "location": parts[2].strip(),
                "duration": parts[3].strip(),
                "description": [],  # We'll append descriptions
                "link": ""  # Handle link extraction if any
            }
        return None

    def parse_projects_data(self, text):
        """
        Parses project-related information from the provided text.
        """
        # Format: Title | Duration
        parts = text.split(" | ")
        if len(parts) >= 2:
            return {
                "title": parts[0].strip(),
                "duration": parts[1].strip(),
                "description": [],  # Add project descriptions
                "link": ""  # Handle link if available
            }
        return None
