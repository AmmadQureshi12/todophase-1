"""Command handlers for todo operations."""
from typing import List, Tuple
from todoapp.storage import TodoStorage
from todoapp.models import Todo
from todoapp.validators import validate_description


def add_todo(storage: TodoStorage, description: str) -> Tuple[bool, str]:
    """Add a new todo to storage.

    Args:
        storage: The TodoStorage instance
        description: The todo description text

    Returns:
        Tuple of (success, message)
        - (True, success_message) if todo was added
        - (False, error_message) if validation failed
    """
    # Validate description
    is_valid, error_msg = validate_description(description)
    if not is_valid:
        return False, error_msg

    try:
        todo = storage.add(description)
        return True, f"Todo added successfully (ID: {todo.id})"
    except ValueError as e:
        return False, str(e)


def list_todos(storage: TodoStorage) -> List[Todo]:
    """Get all todos from storage.

    Args:
        storage: The TodoStorage instance

    Returns:
        List of all Todo objects
    """
    return storage.get_all()


def mark_complete(storage: TodoStorage, todo_id: int) -> Tuple[bool, str]:
    """Mark a todo as complete.

    Args:
        storage: The TodoStorage instance
        todo_id: The ID of the todo to mark complete

    Returns:
        Tuple of (success, message)
        - (True, success_message) if todo was marked complete
        - (False, error_message) if todo not found
    """
    if storage.mark_complete(todo_id):
        return True, "Todo marked as complete"
    return False, f"Todo with ID {todo_id} not found"


def update_todo(storage: TodoStorage, todo_id: int, new_description: str) -> Tuple[bool, str]:
    """Update a todo's description.

    Args:
        storage: The TodoStorage instance
        todo_id: The ID of the todo to update
        new_description: The new description text

    Returns:
        Tuple of (success, message)
        - (True, success_message) if todo was updated
        - (False, error_message) if validation failed or todo not found
    """
    # Validate description
    is_valid, error_msg = validate_description(new_description)
    if not is_valid:
        return False, error_msg

    try:
        if storage.update(todo_id, new_description):
            return True, "Todo updated successfully"
        return False, f"Todo with ID {todo_id} not found"
    except ValueError as e:
        return False, str(e)


def delete_todo(storage: TodoStorage, todo_id: int) -> Tuple[bool, str]:
    """Delete a todo from storage.

    Args:
        storage: The TodoStorage instance
        todo_id: The ID of the todo to delete

    Returns:
        Tuple of (success, message)
        - (True, success_message) if todo was deleted
        - (False, error_message) if todo not found
    """
    if storage.delete(todo_id):
        return True, "Todo deleted successfully"
    return False, f"Todo with ID {todo_id} not found"
