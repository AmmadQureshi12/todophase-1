"""Input validation utilities."""
from typing import Tuple


def validate_description(description: str) -> Tuple[bool, str]:
    """Validate a todo description.

    Args:
        description: The description text to validate

    Returns:
        Tuple of (is_valid, error_message)
        - (True, "") if valid
        - (False, error_message) if invalid
    """
    if not isinstance(description, str):
        return False, "Description must be a string"

    description_stripped = description.strip()
    if not description_stripped:
        return False, "Description cannot be empty"

    if len(description) > 500:
        return False, "Description cannot exceed 500 characters"

    return True, ""


def validate_todo_id(todo_id_str: str) -> Tuple[bool, int, str]:
    """Validate and parse a todo ID from user input.

    Args:
        todo_id_str: The ID string from user input

    Returns:
        Tuple of (is_valid, parsed_id, error_message)
        - (True, id, "") if valid
        - (False, 0, error_message) if invalid
    """
    try:
        todo_id = int(todo_id_str.strip())
        if todo_id < 1:
            return False, 0, "Todo ID must be a positive number"
        return True, todo_id, ""
    except ValueError:
        return False, 0, "Please enter a valid number"


def validate_menu_choice(choice: str, min_val: int, max_val: int) -> Tuple[bool, int, str]:
    """Validate a menu choice from user input.

    Args:
        choice: The choice string from user input
        min_val: Minimum valid value (inclusive)
        max_val: Maximum valid value (inclusive)

    Returns:
        Tuple of (is_valid, parsed_choice, error_message)
        - (True, choice, "") if valid
        - (False, 0, error_message) if invalid
    """
    try:
        choice_int = int(choice.strip())
        if choice_int < min_val or choice_int > max_val:
            return False, 0, f"Please enter a number between {min_val} and {max_val}"
        return True, choice_int, ""
    except ValueError:
        return False, 0, "Please enter a valid number"
