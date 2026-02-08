# Research & Technology Decisions

**Feature**: In-Memory Console-Based Todo Application
**Branch**: 001-todo-cli
**Date**: 2026-02-03

## Overview

This document captures research findings and technology decisions for Phase I of the Todo application. All decisions prioritize simplicity, clarity, and alignment with the project constitution.

## Research Area 1: Python 3.13+ CLI Best Practices

### Question
What are the best practices for building menu-driven console applications in Python 3.13+?

### Research Findings

**Menu-Driven Interface Patterns**:
- Use numbered menu options (1-6) for clarity
- Display menu after each operation for continuous interaction
- Provide clear "Exit" option
- Use `input()` for user prompts with descriptive messages
- Clear screen between operations (optional, but improves UX)

**Input Handling**:
- Use `input().strip()` to remove whitespace
- Validate input immediately after receiving it
- Use try-except for type conversions (e.g., string to int)
- Provide specific error messages for each validation failure

**Error Message Formatting**:
- Prefix errors with "Error: " for clarity
- Use success messages with "Success: " or "✓" prefix
- Keep messages concise (one line preferred)
- Use consistent formatting throughout

### Decision

**Adopt standard Python CLI patterns**:
- Numbered menu with `input()` prompts
- Immediate validation with clear error messages
- Continuous menu loop until user exits
- No external CLI libraries (use standard library only)

**Rationale**: Standard library approach keeps dependencies minimal, is well-understood by beginners, and meets all requirements without added complexity.

**Alternatives Considered**:
- `click` library: Rejected - adds dependency, overkill for menu-driven app
- `argparse`: Rejected - designed for command-line arguments, not interactive menus
- `curses`: Rejected - too complex for requirements, platform compatibility issues

---

## Research Area 2: uv Package Manager

### Question
How should we structure a Python project using the `uv` package manager?

### Research Findings

**Project Initialization**:
- `uv init` creates basic project structure
- `pyproject.toml` is the configuration file
- Supports PEP 621 project metadata

**Dependency Management**:
- `uv add <package>` adds dependencies
- `uv sync` installs dependencies
- Lock file ensures reproducible builds

**Execution Commands**:
- `uv run <script>` executes Python scripts
- `uv run python -m <module>` runs modules
- `uv run pytest` runs tests

**Project Structure**:
- Supports `src/` layout (recommended for packages)
- `pyproject.toml` defines entry points
- Compatible with standard Python packaging

### Decision

**Use `uv` with src/ layout**:
- Initialize with `uv init`
- Place application code in `src/todoapp/`
- Entry point at `src/main.py`
- Configure `pyproject.toml` with project metadata
- Add pytest as dev dependency only

**Rationale**: The src/ layout is a Python best practice that prevents import issues and clearly separates source from tests. `uv` handles this structure natively.

**Alternatives Considered**:
- Flat layout (all code in root): Rejected - less professional, import issues
- Deep package nesting: Rejected - unnecessary for small project

---

## Research Area 3: In-Memory Storage Strategy

### Question
What data structure should we use for in-memory todo storage, and how should we generate IDs?

### Research Findings

**Data Structure Options**:

1. **List of dictionaries**: `[{"id": 1, "description": "...", "completed": False}, ...]`
   - Pros: Simple, JSON-like
   - Cons: O(n) lookups by ID, requires linear search

2. **Dictionary with ID keys**: `{1: {"description": "...", "completed": False}, ...}`
   - Pros: O(1) lookups, updates, deletes by ID
   - Cons: Slightly more memory, need ID generation strategy

3. **List of Todo objects**: `[Todo(id=1, description="...", completed=False), ...]`
   - Pros: Type safety, encapsulation
   - Cons: O(n) lookups by ID

4. **Dictionary of Todo objects**: `{1: Todo(id=1, description="...", completed=False), ...}`
   - Pros: O(1) lookups, type safety, encapsulation
   - Cons: Most complex, but best for maintainability

**ID Generation Strategies**:

1. **Auto-increment counter**: Simple integer counter (1, 2, 3, ...)
   - Pros: Simple, deterministic, user-friendly
   - Cons: Not globally unique (acceptable for single-session)

2. **UUID**: Universally unique identifiers
   - Pros: Globally unique
   - Cons: Not user-friendly, overkill for scope

3. **Timestamp-based**: Use current timestamp
   - Pros: Unique, sortable
   - Cons: Not user-friendly, potential collisions

### Decision

**Use dictionary of Todo objects with auto-increment IDs**:
- Storage: `Dict[int, Todo]` where key is todo ID
- ID generation: Simple counter starting at 1
- Todo class: dataclass or simple class with id, description, completed

**Rationale**:
- O(1) operations meet performance goals
- Type safety improves code quality
- Auto-increment IDs are user-friendly (users reference todos as "1", "2", etc.)
- Dictionary structure simplifies CRUD operations
- Aligns with "production-minded design" principle

**Alternatives Considered**:
- List-based storage: Rejected - O(n) lookups don't scale well
- UUID IDs: Rejected - poor UX for console application

---

## Research Area 4: Testing Strategy

### Question
Should we use pytest or unittest, and how should we organize tests?

### Research Findings

**pytest vs unittest**:

**pytest**:
- Pros: Concise syntax, better assertions, fixtures, widely adopted
- Cons: External dependency (but standard in Python ecosystem)

**unittest**:
- Pros: Standard library, no dependencies
- Cons: More verbose, class-based, less intuitive assertions

**Test Organization Patterns**:

1. **Mirror source structure**: tests/ mirrors src/ structure
   - Pros: Easy to find tests for each module
   - Cons: None for this project size

2. **Flat test directory**: All tests in tests/ root
   - Pros: Simple
   - Cons: Hard to navigate with many test files

3. **By test type**: tests/unit/, tests/integration/, tests/e2e/
   - Pros: Clear test categorization
   - Cons: Overkill for small project

### Decision

**Use pytest with mirrored structure**:
- Testing framework: pytest
- Organization: tests/ mirrors src/todoapp/ structure
- Test files: test_<module>.py for each module
- Integration tests: test_integration.py for end-to-end workflows
- Coverage goal: >80% for core logic

**Rationale**:
- pytest is industry standard and more beginner-friendly
- Mirrored structure makes tests easy to locate
- Single external dependency is acceptable for testing
- Aligns with "developer ergonomics" principle

**Alternatives Considered**:
- unittest: Rejected - more verbose, less intuitive
- No tests: Rejected - violates constitution requirement

---

## Summary of Key Decisions

| Decision Area | Choice | Primary Rationale |
|---------------|--------|-------------------|
| CLI Pattern | Standard library with numbered menu | Minimal dependencies, beginner-friendly |
| Package Manager | uv with src/ layout | Best practice structure, modern tooling |
| Storage Structure | Dict[int, Todo] | O(1) operations, type safety |
| ID Generation | Auto-increment counter | Simple, deterministic, user-friendly |
| Testing Framework | pytest | Industry standard, better DX |
| Test Organization | Mirror source structure | Easy navigation |

## Technology Stack Summary

**Core**:
- Python 3.13+
- Standard library (input/output, data structures)

**Development**:
- uv (package manager)
- pytest (testing framework)

**Dependencies**:
- None for application code
- pytest only for testing (dev dependency)

## Risks & Mitigations

**Risk**: pytest adds external dependency
**Mitigation**: pytest is standard in Python ecosystem; minimal risk
**Fallback**: Can switch to unittest if needed (low effort)

**Risk**: Dictionary storage uses more memory than list
**Mitigation**: Expected scale (1-100 todos) makes memory impact negligible (<1KB)
**Fallback**: None needed for Phase I scope

## Next Steps

1. ✅ Research complete
2. ⏭️ Create data-model.md with Todo entity definition
3. ⏭️ Create quickstart.md with setup instructions
4. ⏭️ Begin implementation following plan.md phases
