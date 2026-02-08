# Todo Application

**Version**: 0.1.0
**Python**: 3.13+
**Package Manager**: uv

## Overview

A clean, deterministic, in-memory console-based Todo application built with Python. This application allows you to manage your tasks through a simple menu-driven interface with five core operations: add, view, update, delete, and mark complete.

**Key Features**:
- ✅ Add new todos with descriptions
- 📋 View all todos with completion status
- ✏️ Update todo descriptions
- 🗑️ Delete todos
- ✓ Mark todos as complete
- 💾 In-memory storage (no persistence)

## Prerequisites

Before you begin, ensure you have:

- **Python 3.13+** installed on your system
- **uv package manager** installed ([installation guide](https://github.com/astral-sh/uv))
- A terminal/console application

### Verify Prerequisites

```bash
# Check Python version (should be 3.13 or higher)
python --version

# Check uv installation
uv --version
```

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd phase1
```

### 2. Install Dependencies

```bash
# Install project dependencies (including dev dependencies)
uv sync
```

### 3. Verify Installation

```bash
# Run the application
uv run src/main.py
```

You should see the welcome message and main menu.

## Usage

### Starting the Application

```bash
uv run src/main.py
```

### Main Menu

When you start the application, you'll see:

```
========================================
  Welcome to Todo Application!
========================================

Manage your tasks with ease.
Choose an option from the menu below.

========================================
         Todo Application
========================================
1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Todo Complete
6. Exit
========================================
```

### Operations

#### 1. Add Todo

Add a new task to your list.

```
Enter your choice (1-6): 1
Enter todo description: Buy groceries

✓ Todo added successfully (ID: 1)
```

#### 2. View Todos

Display all your todos with their status.

```
Enter your choice (1-6): 2

========================================
         Your Todos
========================================
[1] Buy groceries
    Status: Pending
[2] Call mom
    Status: ✓ Completed
========================================
```

**Empty List**:
```
Enter your choice (1-6): 2

No todos found. Add one to get started!
```

#### 3. Update Todo

Modify the description of an existing todo.

```
Enter your choice (1-6): 3
Enter todo ID: 1
Enter new description: Buy groceries and cook dinner

✓ Todo updated successfully
```

#### 4. Delete Todo

Remove a todo from your list.

```
Enter your choice (1-6): 4
Enter todo ID: 1

✓ Todo deleted successfully
```

#### 5. Mark Todo Complete

Mark a task as completed.

```
Enter your choice (1-6): 5
Enter todo ID: 1

✓ Todo marked as complete
```

#### 6. Exit

Exit the application gracefully.

```
Enter your choice (1-6): 6

========================================
  Thank you for using Todo Application!
========================================

Goodbye!
```

## Example Workflows

### Workflow 1: Basic Todo Management

```bash
# Start the application
uv run src/main.py

# Add a todo
1 → "Buy groceries"

# Add another todo
1 → "Call mom"

# View all todos
2 → See both todos listed

# Mark first todo complete
5 → Enter ID: 1

# View todos again
2 → See "Buy groceries" marked as completed

# Exit
6
```

### Workflow 2: Update and Delete

```bash
# Start application
uv run src/main.py

# Add a todo
1 → "Finish report"

# Update the todo
3 → ID: 1 → "Finish quarterly report"

# View to confirm
2 → See updated description

# Delete the todo
4 → ID: 1

# View to confirm deletion
2 → Empty list

# Exit
6
```

### Workflow 3: Multiple Todos

```bash
# Start application
uv run src/main.py

# Add multiple todos
1 → "Task A"
1 → "Task B"
1 → "Task C"

# View all
2 → See all 3 todos

# Mark some complete
5 → ID: 2
5 → ID: 3

# View final state
2 → See 1 pending, 2 completed

# Exit
6
```

## Error Handling

The application handles various error scenarios gracefully:

### Invalid Menu Choice
```
Enter your choice (1-6): 9
Error: Please enter a number between 1 and 6
```

### Empty Description
```
Enter todo description:
Error: Description cannot be empty
```

### Description Too Long
```
Enter todo description: [501 characters]
Error: Description cannot exceed 500 characters
```

### Invalid Todo ID
```
Enter todo ID: 999
Error: Todo with ID 999 not found
```

### Non-Numeric Input
```
Enter todo ID: abc
Error: Please enter a valid number
```

### Keyboard Interrupt (Ctrl+C)
```
^C
========================================
  Application interrupted by user
========================================

Goodbye!
```

## Project Structure

```
phase1/
├── src/
│   ├── todoapp/
│   │   ├── __init__.py
│   │   ├── models.py        # Todo entity
│   │   ├── storage.py       # In-memory storage
│   │   ├── commands.py      # Command handlers
│   │   ├── cli.py           # CLI interface
│   │   └── validators.py    # Input validation
│   └── main.py              # Entry point
├── tests/
│   └── __init__.py
├── docs/
│   └── README.md            # This file
├── pyproject.toml           # Project configuration
└── .gitignore               # Git ignore rules
```

## Development

### Running Tests

```bash
# Run all tests (when implemented)
uv run pytest

# Run with coverage
uv run pytest --cov=src/todoapp

# Run specific test file
uv run pytest tests/test_models.py
```

### Code Quality

The codebase follows Python best practices:
- **Type hints**: All functions have type annotations
- **Docstrings**: All modules, classes, and functions are documented
- **Validation**: Input validation at all entry points
- **Error handling**: Graceful error messages for all failure cases
- **Separation of concerns**: Clear module boundaries (models, storage, commands, CLI, validators)

## Technical Details

### Data Model

**Todo Entity**:
- `id` (int): Unique identifier (auto-generated, starts at 1)
- `description` (str): Task description (1-500 characters)
- `completed` (bool): Completion status (default: False)

**Storage**:
- In-memory dictionary: `Dict[int, Todo]`
- O(1) operations for add, get, update, delete
- Auto-incrementing ID counter

### Validation Rules

**Description**:
- Minimum: 1 character (after stripping whitespace)
- Maximum: 500 characters
- Must be non-empty string

**Todo ID**:
- Must be a positive integer
- Must exist in storage for operations

### Performance

- **Startup time**: < 2 seconds
- **Operation speed**: Instant (all operations are O(1) or O(n) for display)
- **Memory usage**: Minimal (~100-600 bytes per todo)
- **Scalability**: Optimized for 1-100 todos per session

## Limitations

### Phase I Constraints

- **No Persistence**: All data is lost when the application exits
- **Single User**: No multi-user support or concurrent access
- **No Undo**: Cannot undo operations
- **No Uncomplete**: Cannot mark a completed todo as incomplete
- **No Search**: Cannot search or filter todos
- **No Categories**: Cannot organize todos into categories or tags
- **No Due Dates**: Cannot set due dates or priorities

These limitations are intentional for Phase I. Future phases will add persistence, web interface, and advanced features.

## Troubleshooting

### Issue: "uv: command not found"

**Solution**: Install uv package manager
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Issue: "Python version not supported"

**Solution**: Ensure Python 3.13+ is installed
```bash
# Check current version
python --version

# Install Python 3.13+ from python.org
```

### Issue: "Module not found" errors

**Solution**: Ensure dependencies are installed
```bash
uv sync
```

### Issue: Application doesn't start

**Solution**: Check for syntax errors
```bash
# Run Python directly to see error messages
uv run python src/main.py
```

## License

This project is part of a learning exercise for building clean, maintainable Python applications.

## Support

For issues or questions, please refer to:
- [Specification](../specs/001-todo-cli/spec.md)
- [Implementation Plan](../specs/001-todo-cli/plan.md)
- [Data Model](../specs/001-todo-cli/data-model.md)

---

**Version**: 0.1.0
**Last Updated**: 2026-02-03
**Phase**: I (In-Memory Console Application)
