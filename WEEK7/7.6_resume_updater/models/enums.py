from enum import Enum

class FileType(Enum):
    """
    This enumeration represents different types of file formats that can be used.

    Attributes:
        DOCX (str): Represents a Microsoft Word document file with the ".docx" extension.
        HTML (str): Represents an HTML file with the ".html" extension.
    """
    DOCX = "docx"   
    HTML = "html"
    
class SectionType(Enum):
    """
    SectionType is an enumeration that represents different sections of a resume.

    Attributes:
        EDUCATION: Represents the "Education" section of my resume.
        EXPERIENCE: Represents the "Experience" section of my resume.
        SKILLS: Represents the "Skills" section of my resume.
        PROJECTS: Represents the "Projects" section of my resume.
    """
    EDUCATION = "Education"
    EXPERIENCE = "Experience"
    SKILLS_AND_INTERESTS = "Skills & Interests"
    LEADERSHIP_AND_ACTIVITIES = "Leadership & Activities"
    PROJECTS = "Projects"
