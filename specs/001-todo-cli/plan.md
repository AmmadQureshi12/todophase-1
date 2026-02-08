# Implementation Plan: In-Memory Console-Based Todo Application

**Branch**: `001-todo-cli` | **Date**: 2026-02-03 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-todo-cli/spec.md`

## Summary

Build a clean, deterministic, in-memory Python console Todo application with all five core operations (add, delete, update, view, mark complete) using Python 3.13+ and the `uv` package manager. The application prioritizes code quality, maintainability, and clear structure for beginner-to-intermediate Python developers. All data is stored in memory only with no persistence across sessions.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Python standard library only (no external dependencies for core functionality)
**Storage**: In-memory data structures (list or dictionary)
**Testing**: pytest (preferred) or unittest
**Target Platform**: Cross-platform console/terminal (Windows, macOS, Linux)
**Project Type**: Single project (console application)
**Performance Goals**: Application startup in under 2 seconds; operations complete instantly
**Constraints**: No file I/O, no database connections, no external storage; 500 character maximum for todo descriptions; single-user only
**Scale/Scope**: Single-user application; expected usage of 1-100 todos per session; session-based lifecycle only

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Phase I Constraints Validation

| Constraint | Requirement | Status |
|------------|-------------|--------|
| Language | Python | ✅ PASS - Python 3.13+ specified |
| Interface | Console-based CLI | ✅ PASS - Menu-driven console interface |
| Storage | In-memory only | ✅ PASS - No filesystem or database usage |
| Features | Create, list, update, delete, mark complete | ✅ PASS - All five operations specified |
| Focus | Clean logic, clear data models | ✅ PASS - Emphasis on code quality and structure |

### Core Principles Validation

| Principle | Alignment | Evidence |
|-----------|-----------|----------|
| I. Simplicity First | ✅ PASS | Minimal dependencies, straightforward CLI, no over-engineering |
| II. Separation of Concerns | ✅ PASS | Planned modules: models, storage, commands, main |
| III. Incremental Evolution | ✅ PASS | Phase I foundation for future phases |
| IV. Production-Minded Design | ✅ PASS | Input validation, error handling, clear messages required |
| V. Developer Ergonomics | ✅ PASS | Code readability is explicit success criterion |
| VI. Safety and Determinism | ✅ PASS | Deterministic in-memory operations, no side effects |

**Gate Result**: ✅ PASS - All constitution requirements satisfied. No violations to justify.

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-cli/
├── spec.md              # Feature specification
├── plan.md              # This file (architectural plan)
├── research.md          # Phase 0 output (technology decisions)
├── data-model.md        # Phase 1 output (entity design)
├── quickstart.md        # Phase 1 output (setup and usage guide)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── todoapp/
│   ├── __init__.py
│   ├── models.py        # Todo entity and data structures
│   ├── storage.py       # In-memory storage abstraction
│   ├── commands.py      # Command handlers (add, delete, update, etc.)
│   ├── cli.py           # CLI interface and menu system
│   └── validators.py    # Input validation logic
└── main.py              # Application entry point

tests/
├── __init__.py
├── test_models.py       # Todo entity tests
├── test_storage.py      # Storage operations tests
├── test_commands.py     # Command handler tests
├── test_validators.py   # Validation logic tests
└── test_integration.py  # End-to-end workflow tests

pyproject.toml           # uv project configuration
README.md                # Project documentation
.gitignore               # Git ignore rules
```

**Structure Decision**: Single project structure selected. This is a standalone console application with no frontend/backend split. The `src/todoapp/` package contains all application logic organized by responsibility (models, storage, commands, CLI, validation). Tests mirror the source structure for clarity. The `main.py` entry point at the root provides a clean execution interface via `uv run main.py`.

## Complexity Tracking

No constitution violations. This section is not applicable.

## Phase 0: Research & Technology Decisions

### Research Areas

1. **Python 3.13+ CLI Best Practices**
   - Menu-driven interface patterns
   - Input handling and validation
   - Error message formatting

2. **uv Package Manager**
   - Project initialization
   - Dependency management (if any)
   - Execution commands

3. **In-Memory Storage Strategy**
   - Data structure selection (list vs dictionary)
   - ID generation strategy
   - Performance characteristics

4. **Testing Strategy**
   - pytest vs unittest selection
   - Test organization patterns
   - Coverage expectations

### Decisions Summary

See [research.md](./research.md) for detailed research findings and rationale.

## Phase 1: Design & Contracts

### Data Model

See [data-model.md](./data-model.md) for complete entity definitions, validation rules, and state transitions.

### API Contracts

**Note**: This is a console application with no external API. Internal function contracts are documented in the data model and module docstrings.

### Quick Start Guide

See [quickstart.md](./quickstart.md) for setup instructions, usage examples, and development workflow.

## Implementation Phases

### Phase 1.1: Project Setup
- Initialize Python 3.13+ project with `uv init`
- Create directory structure (src/, tests/)
- Configure pyproject.toml with project metadata
- Set up .gitignore for Python projects
- Create basic README with project description
- Verify `uv run` works with minimal main.py

**Deliverable**: Runnable skeleton project

### Phase 1.2: Data Model & Storage
- Implement Todo class in models.py
  - Fields: id (int), description (str), completed (bool)
  - Validation: description length (1-500 chars)
- Implement TodoStorage class in storage.py
  - In-memory list or dictionary
  - Methods: add, get, get_all, update, delete
  - ID generation strategy (auto-increment)
- Write unit tests for models and storage

**Deliverable**: Tested data layer

### Phase 1.3: Input Validation
- Implement validators.py
  - validate_description: check length and non-empty
  - validate_id: check numeric and exists
  - validate_menu_choice: check valid option
- Write unit tests for validators

**Deliverable**: Tested validation layer

### Phase 1.4: Command Handlers
- Implement commands.py with handler functions
  - add_todo(storage, description)
  - delete_todo(storage, todo_id)
  - update_todo(storage, todo_id, new_description)
  - list_todos(storage)
  - mark_complete(storage, todo_id)
- Each handler returns success/failure status and message
- Write unit tests for each command handler

**Deliverable**: Tested business logic layer

### Phase 1.5: CLI Interface
- Implement cli.py with menu system
  - display_menu: show options
  - get_user_input: prompt and validate
  - display_todos: format and print todo list
  - display_message: show success/error messages
- Implement main loop in main.py
  - Initialize storage
  - Display menu
  - Route user input to command handlers
  - Handle exit gracefully
- Write integration tests for full workflows

**Deliverable**: Complete working application

### Phase 1.6: Testing & Documentation
- Achieve test coverage for all modules
- Test edge cases (empty input, invalid IDs, long descriptions)
- Update README with:
  - Installation instructions
  - Usage examples
  - Command reference
  - Development setup
- Verify all success criteria from spec

**Deliverable**: Production-ready Phase I application

## Key Design Decisions

### 1. Storage: Dictionary vs List

**Decision**: Use dictionary with integer keys for O(1) lookups

**Rationale**:
- Dictionary provides constant-time access by ID
- Simplifies delete and update operations
- ID generation via max(keys) + 1 or counter
- List would require linear search for ID-based operations

**Trade-off**: Slightly more memory overhead, but negligible for expected scale (1-100 todos)

### 2. ID Generation Strategy

**Decision**: Auto-incrementing integer counter

**Rationale**:
- Simple and deterministic
- No external dependencies (no UUID library needed)
- User-friendly (IDs are 1, 2, 3, not UUIDs)
- Sufficient for single-user, single-session application

**Trade-off**: IDs reset each session (acceptable per spec)

### 3. Module Organization

**Decision**: Separate modules for models, storage, commands, CLI, validators

**Rationale**:
- Clear separation of concerns (constitution principle II)
- Each module has single responsibility
- Easy to test in isolation
- Easy for new developers to navigate (success criterion SC-002)

**Trade-off**: More files, but improved maintainability

### 4. Error Handling Strategy

**Decision**: Return (success: bool, message: str) tuples from command handlers

**Rationale**:
- Explicit error handling without exceptions for control flow
- Clear success/failure states
- Easy to test
- Allows CLI layer to format messages consistently

**Trade-off**: Slightly more verbose than exceptions, but more predictable

### 5. Testing Framework

**Decision**: pytest

**Rationale**:
- More concise syntax than unittest
- Better assertion introspection
- Fixture support for test setup
- Industry standard for modern Python projects

**Trade-off**: External dependency, but minimal and standard

### 6. Input Validation Location

**Decision**: Separate validators.py module

**Rationale**:
- Reusable validation logic
- Testable in isolation
- Clear validation rules
- Separates validation from business logic

**Trade-off**: Additional module, but improves clarity

## Risk Analysis

### Risk 1: Unicode Handling in Console

**Impact**: Medium - Special characters may not display correctly on all terminals

**Mitigation**:
- Use UTF-8 encoding explicitly
- Test on Windows, macOS, Linux terminals
- Document encoding requirements in README

**Contingency**: Provide ASCII-only mode if needed in future phases

### Risk 2: User Input Edge Cases

**Impact**: Low - Invalid input could cause crashes

**Mitigation**:
- Comprehensive input validation
- Try-except blocks for input parsing
- Clear error messages for all invalid inputs
- Extensive edge case testing

**Contingency**: Add input sanitization if issues discovered

### Risk 3: ID Collision After Many Operations

**Impact**: Very Low - Counter-based IDs could theoretically overflow

**Mitigation**:
- Use Python's arbitrary precision integers (no overflow)
- Expected scale (1-100 todos) makes this impossible

**Contingency**: None needed for Phase I scope

## Success Criteria Mapping

| Success Criterion | Implementation Approach | Verification Method |
|-------------------|------------------------|---------------------|
| SC-001: All five operations functional | Implement all command handlers in Phase 1.4 | Integration tests + manual testing |
| SC-002: Code understandable in 10 min | Clear module organization, docstrings | Code review checklist |
| SC-003: Runs with uv + Python 3.13+ | Configure pyproject.toml correctly | CI/CD or manual verification |
| SC-004: Full workflow in <2 minutes | Efficient menu system, clear prompts | Manual timing test |
| SC-005: Graceful error handling | Validation + error messages | Edge case tests |
| SC-006: No file I/O or database | Code review, no import of file/db libs | Static analysis + review |
| SC-007: Startup in <2 seconds | Minimal dependencies, no heavy imports | Timing measurement |

## Next Steps

1. ✅ Complete Phase 0 research (see research.md)
2. ✅ Complete Phase 1 design (see data-model.md)
3. ✅ Create quickstart guide (see quickstart.md)
4. ⏭️ Run `/sp.tasks` to generate actionable task breakdown
5. ⏭️ Execute implementation following task order
6. ⏭️ Verify all success criteria before phase completion

## Architectural Decision Records

No ADRs required for Phase I. Design decisions are straightforward and follow standard Python CLI patterns. If significant architectural decisions arise during implementation (e.g., major refactoring needs), document them as ADRs in `history/adr/`.
