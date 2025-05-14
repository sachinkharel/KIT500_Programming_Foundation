from dataclasses import dataclass, field


@dataclass
class ResumeSection:
    """
    A dataclass representing a section of a resume.
    
    This class provides a structured way to store and access different sections
    of a resume, such as Education, Experience, Skills, etc.
    
    Attributes:
        section_type (str): The type of section (e.g., "Education", "Experience").
        entries (List[Dict]): A list of dictionaries containing the entries for this section.
    """
    section_type: str
    entries: list[dict] = field(default_factory=list)
    
    def add_entry(self, entry: dict) -> None:
        """
        Add a new entry to this section.
        
        Args:
            entry (Dict): The entry to add to this section.
        """
        self.entries.append(entry)
    
    def to_dict(self) -> dict:
        """
        Convert this section to a dictionary for JSON serialization.
        
        Returns:
            Dict: A dictionary representation of this section.
        """
        return {
            "section_type": self.section_type,
            "entries": self.entries,
        }


@dataclass
class ResumeDocument:
    """
    A dataclass representing a complete resume document.
    
    This class provides a structured way to store and access all sections
    of a resume, as well as metadata about the resume document itself.
    
    Attributes:
        file_path (str): The path to the resume file.
        sections (Dict[str, ResumeSection]): A dictionary mapping section types to ResumeSection objects.
    """
    file_path: str
    sections: dict[str, ResumeSection] = field(default_factory=dict)
    
    def add_section(self, section: ResumeSection) -> None:
        """
        Add a new section to this resume document.
        
        Args:
            section (ResumeSection): The section to add to this resume document.
        """
        self.sections[section.section_type] = section
        
        """example output
        {
            "section_type": "Education",
            "entries": [
                {"degree": "Bachelor of Science", "institution": "XYZ University", "year": 2020},
                {"degree": "Master of Science", "institution": "ABC University", "year": 2022}
            ]
        }
        """
    
    def get_section(self, section_type: str) -> ResumeSection:
        """
        Get a section from this resume document by its type.
        
        Args:
            section_type (str): The type of section to get.
            
        Returns:
            Optional[ResumeSection]: The requested section, or None if it doesn't exist.
        """
        
        """
        example output
        {
            "section_type": "Education",
            "entries": [
                {"degree": "Bachelor of Science", "institution": "XYZ University", "year": 2020},
                {"degree": "Master of Science", "institution": "ABC University", "year": 2022}
            ]
        }
        """
        section = self.sections.get(section_type)
        if section is None:
            raise ValueError(f"Section of type '{section_type}' not found.")
        return section
    
    
    
    def to_dict(self) -> dict:
        """
        Convert this resume document to a dictionary for JSON serialization.
        
        Returns:
            Dict: A dictionary representation of this resume document.
        """
         
        return {
            "sections": {section_type: section.to_dict() for section_type, section in self.sections.items()},
        }