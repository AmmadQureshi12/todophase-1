"""In-memory storage for todo items."""
from typing import Dict, List, Optional
from todoapp.models import Todo


class TodoStorage:
    """In-memory storage for todo items.

    Manages a collection of todos with CRUD operations.
    Uses a dictionary for O(1) lookups by ID.
    """

    def __init__(self):
        """Initialize empty storage."""
        self._todos: Dict[int, Todo] = {}
        self._next_id: int = 1

    def add(self, description: str) -> Todo:
        """Add a new todo and return it.

        Args:
            description: The todo description text

        Returns:
            The created Todo object

        Raises:
            ValueError: If description is invalid
        """
        todo = Todo(id=self._next_id, description=description, completed=False)
        self._todos[self._next_id] = todo
        self._next_id += 1
        return todo

    def get(self, todo_id: int) -> Optional[Todo]:
        """Get a todo by ID, or None if not found.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The Todo object if found, None otherwise

        Raises:
            ValueError: If todo_id is not a positive integer
        """
        if not isinstance(todo_id, int) or todo_id < 1:
            raise ValueError("Todo ID must be a positive integer")
        return self._todos.get(todo_id)

    def get_all(self) -> List[Todo]:
        """Get all todos as a list.

        Returns:
            List of all Todo objects (empty list if none exist)
        """
        return list(self._todos.values())

    def exists(self, todo_id: int) -> bool:
        """Check if a todo exists.

        Args:
            todo_id: The ID to check

        Returns:
            True if todo exists, False otherwise
        """
        return todo_id in self._todos

    def count(self) -> int:
        """Return the total number of todos.

        Returns:
            The count of todos in storage
        """
        return len(self._todos)

    def mark_complete(self, todo_id: int) -> bool:
        """Mark a todo as complete.

        Args:
            todo_id: The ID of the todo to mark complete

        Returns:
            True if successful, False if todo not found
        """
        todo = self.get(todo_id)
        if todo is None:
            return False
        todo.mark_complete()
        return True

    def update(self, todo_id: int, new_description: str) -> bool:
        """Update a todo's description.

        Args:
            todo_id: The ID of the todo to update
            new_description: The new description text

        Returns:
            True if successful, False if todo not found

        Raises:
            ValueError: If new_description is invalid
        """
        todo = self.get(todo_id)
        if todo is None:
            return False
        todo.update_description(new_description)
        return True

    def delete(self, todo_id: int) -> bool:
        """Delete a todo.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if successful, False if todo not found
        """
        if todo_id in self._todos:
            del self._todos[todo_id]
            return True
        return False
