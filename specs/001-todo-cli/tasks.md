---
description: "Task list for In-Memory Console-Based Todo Application"
---

# Tasks: In-Memory Console-Based Todo Application

**Input**: Design documents from `/specs/001-todo-cli/`
**Prerequisites**: plan.md, spec.md, data-model.md, research.md, quickstart.md

**Tests**: Tests are NOT included in this task list as they were not explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- Single project structure with `src/todoapp/` for application code
- Entry point at `src/main.py`
- Tests in `tests/` directory
- Configuration in `pyproject.toml`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Initialize Python 3.13+ project using `uv init` in repository root
- [X] T002 Create directory structure: src/todoapp/, tests/, docs/
- [X] T003 [P] Create __init__.py files in src/todoapp/ and tests/
- [X] T004 [P] Configure pyproject.toml with project metadata (name, version, Python 3.13+ requirement)
- [X] T005 [P] Create .gitignore for Python projects (exclude __pycache__, *.pyc, .pytest_cache, etc.)
- [X] T006 [P] Add pytest as dev dependency using `uv add --dev pytest`
- [X] T007 Create minimal src/main.py entry point with print statement to verify setup
- [X] T008 Verify project runs with `uv run src/main.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T009 [P] Create Todo dataclass in src/todoapp/models.py with fields: id (int), description (str), completed (bool)
- [X] T010 [P] Add __post_init__ validation to Todo class for id (positive integer), description (1-500 chars, non-empty after strip), completed (boolean)
- [X] T011 [P] Add mark_complete() method to Todo class in src/todoapp/models.py
- [X] T012 [P] Add update_description() method to Todo class in src/todoapp/models.py with validation
- [X] T013 Create TodoStorage class in src/todoapp/storage.py with __init__ method (initialize _todos dict and _next_id counter)
- [X] T014 [P] Implement TodoStorage.add(description: str) -> Todo method in src/todoapp/storage.py
- [X] T015 [P] Implement TodoStorage.get(todo_id: int) -> Optional[Todo] method in src/todoapp/storage.py
- [X] T016 [P] Implement TodoStorage.get_all() -> List[Todo] method in src/todoapp/storage.py
- [X] T017 [P] Implement TodoStorage.exists(todo_id: int) -> bool method in src/todoapp/storage.py
- [X] T018 [P] Implement TodoStorage.count() -> int method in src/todoapp/storage.py
- [X] T019 Create validators module in src/todoapp/validators.py
- [X] T020 [P] Implement validate_description(description: str) -> tuple[bool, str] in src/todoapp/validators.py
- [X] T021 [P] Implement validate_todo_id(todo_id_str: str) -> tuple[bool, int, str] in src/todoapp/validators.py
- [X] T022 [P] Implement validate_menu_choice(choice: str, min_val: int, max_val: int) -> tuple[bool, int, str] in src/todoapp/validators.py
- [X] T023 Create CLI module in src/todoapp/cli.py with display_menu() function
- [X] T024 [P] Implement display_todos(todos: List[Todo]) function in src/todoapp/cli.py
- [X] T025 [P] Implement display_message(message: str, is_error: bool) function in src/todoapp/cli.py
- [X] T026 [P] Implement get_user_input(prompt: str) -> str function in src/todoapp/cli.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and View Todos (Priority: P1) 🎯 MVP

**Goal**: Enable users to quickly capture tasks and see their todo list without any setup or configuration

**Independent Test**: Launch the application, add one or more todos using menu option 1, view the list using menu option 2. Verify todos are displayed with IDs, descriptions, and completion status.

### Implementation for User Story 1

- [X] T027 [P] [US1] Create commands module in src/todoapp/commands.py
- [X] T028 [P] [US1] Implement add_todo(storage: TodoStorage, description: str) -> tuple[bool, str] in src/todoapp/commands.py
- [X] T029 [P] [US1] Implement list_todos(storage: TodoStorage) -> List[Todo] in src/todoapp/commands.py
- [X] T030 [US1] Implement main application loop in src/main.py (initialize storage, display menu, handle exit)
- [X] T031 [US1] Add menu option 1 handler in src/main.py to call add_todo command (prompt for description, validate, display result)
- [X] T032 [US1] Add menu option 2 handler in src/main.py to call list_todos and display results
- [X] T033 [US1] Add menu option 6 handler in src/main.py for graceful exit
- [X] T034 [US1] Add invalid menu choice handling in src/main.py with error message
- [X] T035 [US1] Add help/instructions display on startup in src/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently. Users can add and view todos.

---

## Phase 4: User Story 2 - Mark Todos as Complete (Priority: P2)

**Goal**: Enable users to track progress by marking completed tasks, helping them see what's done and what remains

**Independent Test**: Add todos using US1 functionality, then mark some as complete using menu option 5. Verify completion status is reflected in the list view.

### Implementation for User Story 2

- [X] T036 [US2] Implement TodoStorage.mark_complete(todo_id: int) -> bool method in src/todoapp/storage.py
- [X] T037 [US2] Implement mark_complete(storage: TodoStorage, todo_id: int) -> tuple[bool, str] in src/todoapp/commands.py
- [X] T038 [US2] Add menu option 5 handler in src/main.py to call mark_complete command (prompt for ID, validate, display result)
- [X] T039 [US2] Update display_todos() in src/todoapp/cli.py to clearly show completion status (e.g., "[✓]" or "(Completed)")

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently. Users can add, view, and mark todos complete.

---

## Phase 5: User Story 3 - Update Todo Descriptions (Priority: P3)

**Goal**: Enable users to modify task descriptions when requirements change or initial entries contain errors

**Independent Test**: Add a todo using US1 functionality, then update its description using menu option 3. Verify the change persists in the list view.

### Implementation for User Story 3

- [X] T040 [US3] Implement TodoStorage.update(todo_id: int, new_description: str) -> bool method in src/todoapp/storage.py
- [X] T041 [US3] Implement update_todo(storage: TodoStorage, todo_id: int, new_description: str) -> tuple[bool, str] in src/todoapp/commands.py
- [X] T042 [US3] Add menu option 3 handler in src/main.py to call update_todo command (prompt for ID and new description, validate both, display result)

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently. Users can add, view, mark complete, and update todos.

---

## Phase 6: User Story 4 - Delete Todos (Priority: P4)

**Goal**: Enable users to remove tasks that are no longer relevant or were added by mistake

**Independent Test**: Add todos using US1 functionality, then delete specific ones using menu option 4. Verify they no longer appear in the list.

### Implementation for User Story 4

- [X] T043 [US4] Implement TodoStorage.delete(todo_id: int) -> bool method in src/todoapp/storage.py
- [X] T044 [US4] Implement delete_todo(storage: TodoStorage, todo_id: int) -> tuple[bool, str] in src/todoapp/commands.py
- [X] T045 [US4] Add menu option 4 handler in src/main.py to call delete_todo command (prompt for ID, validate, display result)

**Checkpoint**: All user stories should now be independently functional. Users can perform all five core operations.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and final documentation

- [X] T046 [P] Add docstrings to all classes and functions in src/todoapp/models.py
- [X] T047 [P] Add docstrings to all classes and functions in src/todoapp/storage.py
- [X] T048 [P] Add docstrings to all functions in src/todoapp/commands.py
- [X] T049 [P] Add docstrings to all functions in src/todoapp/cli.py
- [X] T050 [P] Add docstrings to all functions in src/todoapp/validators.py
- [X] T051 [P] Review all error messages for clarity and consistency across all modules
- [X] T052 [P] Add type hints to all function signatures across all modules
- [X] T053 Create docs/README.md with project description, setup instructions using uv, and CLI usage examples
- [X] T054 Add example workflow to docs/README.md demonstrating add/delete/update/list/complete operations
- [X] T055 [P] Add edge case handling for Ctrl+C interruption in src/main.py
- [X] T056 [P] Add handling for extremely long descriptions (>500 chars) with clear error message
- [X] T057 [P] Add handling for special characters and unicode in descriptions
- [X] T058 Verify no file I/O or database operations exist in codebase (code review)
- [X] T059 Test full workflow: add 3 todos, mark 1 complete, update 1, delete 1, view list
- [X] T060 Verify application startup time is under 2 seconds
- [X] T061 Run quickstart.md validation to ensure all documented workflows work correctly

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Integrates with US1 display but independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Uses US1 for testing but independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Uses US1 for testing but independently testable

### Within Each Phase

**Phase 1 (Setup)**:
- T001 must complete before T002-T008
- T002 must complete before T003
- T006 can run anytime after T001
- T007 requires T002-T004 complete
- T008 requires T007 complete

**Phase 2 (Foundational)**:
- Todo model tasks (T009-T012) can run in parallel
- TodoStorage tasks (T013-T018): T013 must complete first, then T014-T018 can run in parallel
- Validator tasks (T019-T022): T019 must complete first, then T020-T022 can run in parallel
- CLI tasks (T023-T026): T023 must complete first, then T024-T026 can run in parallel
- All Phase 2 tasks must complete before any user story work begins

**Phase 3 (US1)**:
- T027-T029 can run in parallel (different functions)
- T030 must complete before T031-T035
- T031-T035 can be implemented sequentially or in parallel

**Phase 4 (US2)**:
- T036-T037 can run in parallel
- T038 requires T036-T037 complete
- T039 can run in parallel with T036-T038

**Phase 5 (US3)**:
- T040-T041 can run in parallel
- T042 requires T040-T041 complete

**Phase 6 (US4)**:
- T043-T044 can run in parallel
- T045 requires T043-T044 complete

**Phase 7 (Polish)**:
- T046-T052 can all run in parallel (different files)
- T053-T054 are sequential (same file)
- T055-T057 can run in parallel (different concerns)
- T058-T061 are verification tasks (run after implementation complete)

### Parallel Opportunities

- **Setup Phase**: T003, T004, T005, T006 can all run in parallel after T002
- **Foundational Phase**: Within each subsystem (models, storage, validators, CLI), tasks marked [P] can run in parallel
- **User Story Phases**: Once Foundational completes, all 4 user stories can be worked on in parallel by different team members
- **Polish Phase**: Documentation tasks (T046-T052) can all run in parallel

---

## Parallel Example: Foundational Phase

```bash
# After T009-T012 (Todo model) complete, launch storage methods in parallel:
Task: "Implement TodoStorage.add() in src/todoapp/storage.py"
Task: "Implement TodoStorage.get() in src/todoapp/storage.py"
Task: "Implement TodoStorage.get_all() in src/todoapp/storage.py"
Task: "Implement TodoStorage.exists() in src/todoapp/storage.py"
Task: "Implement TodoStorage.count() in src/todoapp/storage.py"

# Launch validator functions in parallel:
Task: "Implement validate_description() in src/todoapp/validators.py"
Task: "Implement validate_todo_id() in src/todoapp/validators.py"
Task: "Implement validate_menu_choice() in src/todoapp/validators.py"
```

---

## Parallel Example: User Story 1

```bash
# Launch command implementations in parallel:
Task: "Implement add_todo() in src/todoapp/commands.py"
Task: "Implement list_todos() in src/todoapp/commands.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

**Result**: Working todo app with add and view functionality

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo (now with completion tracking)
4. Add User Story 3 → Test independently → Deploy/Demo (now with editing)
5. Add User Story 4 → Test independently → Deploy/Demo (now with deletion)
6. Complete Polish → Final release

Each story adds value without breaking previous stories.

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (T027-T035)
   - Developer B: User Story 2 (T036-T039)
   - Developer C: User Story 3 (T040-T042)
   - Developer D: User Story 4 (T043-T045)
3. Stories complete and integrate independently
4. Team completes Polish together

---

## Task Summary

**Total Tasks**: 61
- Phase 1 (Setup): 8 tasks
- Phase 2 (Foundational): 18 tasks
- Phase 3 (US1 - Add and View): 9 tasks
- Phase 4 (US2 - Mark Complete): 4 tasks
- Phase 5 (US3 - Update): 3 tasks
- Phase 6 (US4 - Delete): 3 tasks
- Phase 7 (Polish): 16 tasks

**Parallel Opportunities**: 35 tasks marked [P] can run in parallel within their phase

**MVP Scope**: Phases 1-3 (35 tasks) deliver a working todo app with add and view functionality

**Independent Test Criteria**:
- US1: Can add and view todos
- US2: Can mark todos complete and see status
- US3: Can update todo descriptions
- US4: Can delete todos

---

## Notes

- [P] tasks = different files or independent functions, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Tests are NOT included as they were not explicitly requested in the specification
- All file paths use forward slashes for cross-platform compatibility
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
