"""CLI interface utilities."""
from typing import List
from todoapp.models import Todo


def display_menu() -> None:
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("         Todo Application")
    print("=" * 40)
    print("1. Add Todo")
    print("2. View Todos")
    print("3. Update Todo")
    print("4. Delete Todo")
    print("5. Mark Todo Complete")
    print("6. Exit")
    print("=" * 40)


def display_todos(todos: List[Todo]) -> None:
    """Display all todos with their status.

    Args:
        todos: List of Todo objects to display
    """
    if not todos:
        print("\nNo todos found. Add one to get started!")
        return

    print("\n" + "=" * 40)
    print("         Your Todos")
    print("=" * 40)
    for todo in todos:
        status = "[DONE]" if todo.completed else "[PENDING]"
        print(f"[{todo.id}] {todo.description}")
        print(f"    Status: {status}")
    print("=" * 40)


def display_message(message: str, is_error: bool = False) -> None:
    """Display a message to the user.

    Args:
        message: The message text to display
        is_error: Whether this is an error message (default: False)
    """
    prefix = "Error: " if is_error else "[OK] "
    print(f"\n{prefix}{message}")


def get_user_input(prompt: str) -> str:
    """Get input from the user.

    Args:
        prompt: The prompt text to display

    Returns:
        The user's input as a string
    """
    return input(f"\n{prompt}: ").strip()
