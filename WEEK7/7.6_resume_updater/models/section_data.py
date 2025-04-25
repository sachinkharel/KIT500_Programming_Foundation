from dataclasses import dataclass
from models.enums import SectionType

@dataclass
class ResumeSection:
    """
    Represents sections of my resume.
    Attributes:
        section_type (SectionType): The type of the resume section.
        content (str): The content of the resume section.
    """
    section_type: SectionType
    content: str | dict
    
@dataclass
class ResumeUpdateRequest:
    """
    Represents a request to update a resume.
    Attributes:
        sections (list[ResumeSection]): A list of sections to be updated in the resume.
        html_path (str): The path to the HTML file where the updated resume will be saved.    
    """    
    sections: list[ResumeSection]
    html_path: str

@dataclass
class GitChange:
    """
    Represents a change made to a file in a Git repository.
    Attributes:
        commit_message (str): The commit message describing the change.
        file_paths (list[str]): A list of file paths that were changed.
    """
    commit_message: str
    file_paths: list[str]


