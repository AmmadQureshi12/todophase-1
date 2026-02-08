# Quick Start Guide

**Feature**: In-Memory Console-Based Todo Application
**Branch**: 001-todo-cli
**Date**: 2026-02-03

## Overview

This guide provides setup instructions, usage examples, and development workflow for the in-memory console-based Todo application.

## Prerequisites

Before you begin, ensure you have:

- **Python 3.13+** installed on your system
- **uv package manager** installed ([installation guide](https://github.com/astral-sh/uv))
- **Git** for version control
- A terminal/console application

### Verify Prerequisites

```bash
# Check Python version (should be 3.13 or higher)
python --version

# Check uv installation
uv --version

# Check Git installation
git --version
```

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Checkout the Feature Branch

```bash
git checkout 001-todo-cli
```

### 3. Install Dependencies

```bash
# Install project dependencies (including dev dependencies)
uv sync
```

### 4. Verify Installation

```bash
# Run the application
uv run src/main.py

# You should see the main menu
```

## Usage

### Starting the Application

```bash
uv run src/main.py
```

### Main Menu

When you start the application, you'll see a menu like this:

```
=== Todo Application ===
1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Todo Complete
6. Exit

Enter your choice (1-6):
```

### Adding a Todo

1. Select option `1` from the main menu
2. Enter your todo description when prompted
3. The todo will be created with a unique ID

**Example**:
```
Enter your choice (1-6): 1
Enter todo description: Buy groceries
✓ Todo added successfully (ID: 1)
```

### Viewing Todos

1. Select option `2` from the main menu
2. All todos will be displayed with their ID, description, and status

**Example**:
```
Enter your choice (1-6): 2

=== Your Todos ===
[1] Buy groceries (Pending)
[2] Call mom (Completed)
[3] Finish project report (Pending)
```

**Empty List**:
```
Enter your choice (1-6): 2

=== Your Todos ===
No todos found. Add one to get started!
```

### Updating a Todo

1. Select option `3` from the main menu
2. Enter the ID of the todo you want to update
3. Enter the new description

**Example**:
```
Enter your choice (1-6): 3
Enter todo ID: 1
Enter new description: Buy groceries and cook dinner
✓ Todo updated successfully
```

### Deleting a Todo

1. Select option `4` from the main menu
2. Enter the ID of the todo you want to delete
3. Confirm the deletion

**Example**:
```
Enter your choice (1-6): 4
Enter todo ID: 2
✓ Todo deleted successfully
```

### Marking a Todo Complete

1. Select option `5` from the main menu
2. Enter the ID of the todo you want to mark as complete

**Example**:
```
Enter your choice (1-6): 5
Enter todo ID: 1
✓ Todo marked as complete
```

### Exiting the Application

1. Select option `6` from the main menu
2. The application will exit gracefully

**Note**: All todos are stored in memory only. When you exit, all data is lost.

## Common Workflows

### Workflow 1: Basic Todo Management

```
1. Start application: uv run src/main.py
2. Add todo: Choose 1 → "Buy groceries"
3. Add todo: Choose 1 → "Call mom"
4. View todos: Choose 2 → See both todos
5. Mark complete: Choose 5 → Enter ID 1
6. View todos: Choose 2 → See "Buy groceries" as completed
7. Exit: Choose 6
```

### Workflow 2: Update and Delete

```
1. Start application: uv run src/main.py
2. Add todo: Choose 1 → "Finish report"
3. Update todo: Choose 3 → ID 1 → "Finish quarterly report"
4. View todos: Choose 2 → See updated description
5. Delete todo: Choose 4 → ID 1
6. View todos: Choose 2 → Empty list
7. Exit: Choose 6
```

### Workflow 3: Multiple Todos

```
1. Start application: uv run src/main.py
2. Add 3 todos: "Task A", "Task B", "Task C"
3. View all: Choose 2 → See all 3 todos
4. Mark complete: Choose 5 → ID 2
5. Mark complete: Choose 5 → ID 3
6. View all: Choose 2 → See 1 pending, 2 completed
7. Exit: Choose 6
```

## Error Handling

### Invalid Menu Choice

```
Enter your choice (1-6): 9
Error: Invalid choice. Please enter a number between 1 and 6.
```

### Empty Description

```
Enter todo description:
Error: Description cannot be empty.
```

### Description Too Long

```
Enter todo description: [501 characters]
Error: Description cannot exceed 500 characters.
```

### Invalid Todo ID

```
Enter todo ID: 999
Error: Todo with ID 999 not found.
```

### Non-Numeric ID

```
Enter todo ID: abc
Error: Please enter a valid number.
```

## Development Setup

### Project Structure

```
.
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
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_storage.py
│   ├── test_commands.py
│   ├── test_validators.py
│   └── test_integration.py
├── pyproject.toml           # Project configuration
└── README.md                # Project documentation
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src/todoapp

# Run specific test file
uv run pytest tests/test_models.py

# Run with verbose output
uv run pytest -v

# Run and show print statements
uv run pytest -s
```

### Code Quality

```bash
# Format code (if using black)
uv run black src/ tests/

# Lint code (if using ruff)
uv run ruff check src/ tests/

# Type checking (if using mypy)
uv run mypy src/
```

### Development Workflow

1. **Create a new feature branch** (if needed)
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make changes** to the code

3. **Run tests** to ensure nothing breaks
   ```bash
   uv run pytest
   ```

4. **Test manually** by running the application
   ```bash
   uv run src/main.py
   ```

5. **Commit changes**
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

6. **Push to remote** (if applicable)
   ```bash
   git push origin feature/your-feature-name
   ```

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

# Install Python 3.13+ from python.org or use pyenv
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

### Issue: Tests fail

**Solution**: Check test output for specific failures
```bash
# Run tests with verbose output
uv run pytest -v

# Run specific failing test
uv run pytest tests/test_models.py::test_name -v
```

## Performance Notes

- **Startup Time**: Application should start in under 2 seconds
- **Operation Speed**: All operations (add, update, delete) are instant
- **Memory Usage**: Minimal (<1MB for typical usage of 1-100 todos)
- **Scalability**: Designed for 1-100 todos per session; can handle more but not optimized for thousands

## Limitations

### Phase I Constraints

- **No Persistence**: All data is lost when the application exits
- **Single User**: No multi-user support or concurrent access
- **No Undo**: Cannot undo operations (delete is permanent for the session)
- **No Uncomplete**: Cannot mark a completed todo as incomplete
- **No Search**: Cannot search or filter todos (except view all)
- **No Categories**: Cannot organize todos into categories or tags
- **No Due Dates**: Cannot set due dates or priorities

These limitations are intentional for Phase I. Future phases will add persistence, web interface, and advanced features.

## Tips and Best Practices

### For Users

1. **Keep descriptions concise**: Aim for 1-2 sentences per todo
2. **Use the view command frequently**: Check your list after each operation
3. **Mark todos complete as you finish them**: Provides satisfaction and clarity
4. **Delete irrelevant todos**: Keep your list clean and focused

### For Developers

1. **Run tests before committing**: Ensure all tests pass
2. **Follow the module structure**: Keep models, storage, commands, CLI separate
3. **Add tests for new features**: Maintain test coverage
4. **Use type hints**: Improves code clarity and catches errors
5. **Keep functions small**: Single responsibility principle
6. **Document edge cases**: Add comments for non-obvious behavior

## Next Steps

After completing the Quick Start:

1. **Explore the codebase**: Read through each module to understand the structure
2. **Run the test suite**: See how tests are organized and written
3. **Try all features**: Test each menu option to understand the user experience
4. **Review the data model**: Understand the Todo entity and storage layer
5. **Read the implementation plan**: See the phased development approach

## Support

For issues or questions:

1. Check the [README.md](../../README.md) for project overview
2. Review the [specification](./spec.md) for requirements
3. Read the [implementation plan](./plan.md) for architecture details
4. Check the [data model](./data-model.md) for entity definitions

## Version Information

- **Phase**: I (In-Memory Console Application)
- **Python**: 3.13+
- **Package Manager**: uv
- **Testing**: pytest
- **Last Updated**: 2026-02-03
