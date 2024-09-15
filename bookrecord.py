from typing import List, Optional
from dataclasses import dataclass, field

@dataclass
class BookRecord:
    title_author: str = ""
    availability_status: Optional[str] = None
    availability_locations: List[str] = field(default_factory=list)

    # def __init__(self, title_author_str):
    #     # Parse the title_author_str and set attributes
    #     title, author = title_author_str.strip().split(',')
    #     self.title = title.strip()
    #     self.author = author.strip()

    def __post_init__(self):
        valid_statuses = [
            "Available at a preferred location",
            "In-library use only",
            "Available",
            "All copies in use"
        ]
        if self.availability_status and self.availability_status not in valid_statuses:
            raise ValueError(f"Invalid availability status: {self.availability_status}")
        
    def __str__(self):
        return f"{self.title_author} ({self.availability_status})"