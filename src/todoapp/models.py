"""Todo data model."""
from dataclasses import dataclass


@dataclass
class Todo:
    """Represents a single todo item.

    Attributes:
        id: Unique identifier for the todo (positive integer)
        description: The todo task description (1-500 characters)
        completed: Whether the todo is completed (default: False)
    """
    id: int
    description: str
    completed: bool = False

    def __post_init__(self):
        """Validate todo fields after initialization."""
        if not isinstance(self.id, int) or self.id < 1:
            raise ValueError("Todo ID must be a positive integer")

        if not isinstance(self.description, str):
            raise ValueError("Description must be a string")

        description_stripped = self.description.strip()
        if not description_stripped:
            raise ValueError("Description cannot be empty")

        if len(self.description) > 500:
            raise ValueError("Description cannot exceed 500 characters")

        if not isinstance(self.completed, bool):
            raise ValueError("Completed must be a boolean")

    def mark_complete(self) -> None:
        """Mark this todo as completed."""
        self.completed = True

    def update_description(self, new_description: str) -> None:
        """Update the todo description with validation.

        Args:
            new_description: The new description text

        Raises:
            ValueError: If description is invalid
        """
        if not isinstance(new_description, str):
            raise ValueError("Description must be a string")

        description_stripped = new_description.strip()
        if not description_stripped:
            raise ValueError("Description cannot be empty")

        if len(new_description) > 500:
            raise ValueError("Description cannot exceed 500 characters")

        self.description = new_description
