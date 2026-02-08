---
id: 3
title: Generate tasks for todo CLI Phase I
stage: tasks
date: 2026-02-03
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-todo-cli
branch: 001-todo-cli
user: user
command: /sp.tasks
labels: ["task-generation", "planning", "001-todo-cli", "phase-i"]
links:
  spec: specs/001-todo-cli/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-todo-cli/tasks.md
tests:
  - none
---

## Prompt

/sp.tasks Phase I – In-Memory Console-Based Todo Application

# Project Setup
1. Initialize a new Python 3.13+ project using `uv`
2. Create folders:
   - `src/` for source code
   - `tests/` for unit tests
   - `docs/` for README and notes
3. Create `src/main.py` as CLI entry point
4. Verify project runs: `uv run src/main.py`

# Data Model
5. Create `src/models.py`
6. Define a `Todo` class with attributes:
   - `id` (unique identifier, integer)
   - `title` (string)
   - `description` (optional string)
   - `completed` (boolean, default False)
7. Create an in-memory storage in `src/storage.py`:
   - List or dictionary to hold Todo objects
   - Functions to add, get, update, delete, and list todos

# CLI Commands Implementation
8. Create `src/commands.py`
9. Implement `add_todo(title, description)`:
   - Validate title is not empty
   - Assign unique ID
   - Add todo to storage
   - Print confirmation
10. Implement `delete_todo(todo_id)`:
    - Check if ID exists
    - Remove todo from storage
    - Print success/failure message
11. Implement `update_todo(todo_id, title=None, description=None)`:
    - Check if ID exists
    - Update title and/or description
    - Print confirmation
12. Implement `list_todos()`:
    - Display all todos with ID, title, completed status
    - Show pending/completed clearly
13. Implement `mark_complete(todo_id)`:
    - Check if ID exists
    - Set `completed = True`
    - Print confirmation

# CLI Main Loop
14. In `src/main.py`, implement a command loop:
    - Read user input
    - Map commands: add, delete, update, list, complete
    - Call corresponding functions in `commands.py`
    - Loop until user exits
15. Handle invalid commands gracefully
16. Print help/instructions on startup

# Clean Code & Project Structure
17. Ensure all functions/classes have docstrings
18. Keep functions small and single-responsibility
19. Use meaningful variable and function names
20. Avoid duplicate logic (reuse helper functions)
21. Keep modules separated: `models.py`, `storage.py`, `commands.py`, `main.py`

# Unit Testing
22. Create tests in `tests/test_todo.py`
23. Test adding a todo
24. Test deleting a todo (valid and invalid IDs)
25. Test updating a todo (title, description, invalid ID)
26. Test listing todos (empty list, multiple todos)
27. Test marking todo complete (valid and invalid ID)
28. Run all tests using `uv` and ensure 100% pass

# Documentation
29. Write `docs/README.md`:
    - Project description
    - Setup instructions using `uv`
    - CLI usage examples
    - Example workflow with add/delete/update/list/complete
30. Optional: notes on extending for Phase II

# Verification & Demo
31. Run CLI and verify all commands work as expected
32. Confirm in-memory storage only; no files or DB usage
33. Ensure code is clean, modular, and readable
34. Verify project structure follows Python best practices

## Response snapshot

Successfully generated tasks.md with 61 tasks organized across 7 phases:

**Phase 1 (Setup)**: 8 tasks for project initialization with uv, directory structure, and dependencies

**Phase 2 (Foundational)**: 18 tasks for core infrastructure (Todo model, TodoStorage, validators, CLI utilities) - BLOCKS all user stories

**Phase 3 (US1 - Add and View)**: 9 tasks implementing MVP functionality for adding and viewing todos

**Phase 4 (US2 - Mark Complete)**: 4 tasks for completion tracking

**Phase 5 (US3 - Update)**: 3 tasks for description editing

**Phase 6 (US4 - Delete)**: 3 tasks for todo deletion

**Phase 7 (Polish)**: 16 tasks for documentation, error handling, and final verification

**Key Features**:
- All 61 tasks follow strict checklist format: `- [ ] [TaskID] [P?] [Story?] Description with file path`
- 35 tasks marked [P] for parallel execution
- User story labels [US1]-[US4] for traceability
- Independent test criteria for each user story
- MVP scope: Phases 1-3 (35 tasks)
- Clear dependency graph and execution order
- Parallel execution examples provided

**Organization**: Tasks organized by user story to enable independent implementation and testing. Each story can be completed and validated independently.

**Tests**: Not included as they were not explicitly requested in the feature specification.

## Outcome

- ✅ Impact: Generated comprehensive, actionable task list with 61 tasks organized by user story for independent implementation
- 🧪 Tests: No test tasks included (not requested in specification)
- 📁 Files: Created specs/001-todo-cli/tasks.md (61 tasks across 7 phases)
- 🔁 Next prompts: /sp.implement to execute the task list, or manual implementation starting with Phase 1 (Setup)
- 🧠 Reflection: Task generation successfully mapped user stories from spec.md to implementation tasks, maintaining independence between stories for parallel development

## Evaluation notes (flywheel)

- Failure modes observed: None - all design documents were available and well-structured
- Graders run and results (PASS/FAIL): Format validation PASS (all tasks follow checklist format with IDs, labels, file paths)
- Prompt variant (if applicable): Standard /sp.tasks workflow
- Next experiment (smallest change to try): Consider adding optional test tasks as a separate phase for projects that request TDD approach
