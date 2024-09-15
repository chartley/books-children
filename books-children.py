from typing import List, Optional
from dataclasses import dataclass, field

@dataclass
class Book:
    title_author: str = ""
    availability_status: Optional[str] = None
    availability_locations: List[str] = field(default_factory=list)

    def __post_init__(self):
        valid_statuses = [
            "Available at a preferred location",
            "In-library use only",
            "Available",
            "All copies in use"
        ]
        if self.availability_status and self.availability_status not in valid_statuses:
            raise ValueError(f"Invalid availability status: {self.availability_status}")

def main():
    print("How are ya, mate?")

    # load titles
    titles = import_titles()
    print("Titles:", titles[:3])

    # for each title, search the library, determine availability

def import_titles(file_path="titles.txt"):
    return open(file_path, "r").readlines()

if __name__ == "__main__":
    main()