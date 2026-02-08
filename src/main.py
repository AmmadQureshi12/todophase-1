"""Todo Application Entry Point."""
from todoapp.storage import TodoStorage
from todoapp.cli import display_menu, display_todos, display_message, get_user_input
from todoapp.validators import validate_menu_choice, validate_todo_id
from todoapp.commands import add_todo, list_todos, mark_complete, update_todo, delete_todo


def main():
    """Main entry point for the todo application."""
    # Initialize storage
    storage = TodoStorage()

    # Display welcome message
    print("\n" + "=" * 40)
    print("  Welcome to Todo Application!")
    print("=" * 40)
    print("\nManage your tasks with ease.")
    print("Choose an option from the menu below.")

    # Main application loop
    while True:
        try:
            # Display menu
            display_menu()

            # Get user choice
            choice_str = get_user_input("Enter your choice (1-6)")

            # Validate menu choice
            is_valid, choice, error_msg = validate_menu_choice(choice_str, 1, 6)
            if not is_valid:
                display_message(error_msg, is_error=True)
                continue

            # Handle menu options
            if choice == 1:
                # Add todo
                description = get_user_input("Enter todo description")
                success, message = add_todo(storage, description)
                display_message(message, is_error=not success)

            elif choice == 2:
                # View todos
                todos = list_todos(storage)
                display_todos(todos)

            elif choice == 3:
                # Update todo
                todo_id_str = get_user_input("Enter todo ID")
                is_valid, todo_id, error_msg = validate_todo_id(todo_id_str)
                if not is_valid:
                    display_message(error_msg, is_error=True)
                    continue

                new_description = get_user_input("Enter new description")
                success, message = update_todo(storage, todo_id, new_description)
                display_message(message, is_error=not success)

            elif choice == 4:
                # Delete todo
                todo_id_str = get_user_input("Enter todo ID")
                is_valid, todo_id, error_msg = validate_todo_id(todo_id_str)
                if not is_valid:
                    display_message(error_msg, is_error=True)
                    continue

                success, message = delete_todo(storage, todo_id)
                display_message(message, is_error=not success)

            elif choice == 5:
                # Mark todo complete
                todo_id_str = get_user_input("Enter todo ID")
                is_valid, todo_id, error_msg = validate_todo_id(todo_id_str)
                if not is_valid:
                    display_message(error_msg, is_error=True)
                    continue

                success, message = mark_complete(storage, todo_id)
                display_message(message, is_error=not success)

            elif choice == 6:
                # Exit
                print("\n" + "=" * 40)
                print("  Thank you for using Todo Application!")
                print("=" * 40)
                print("\nGoodbye!\n")
                break

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n" + "=" * 40)
            print("  Application interrupted by user")
            print("=" * 40)
            print("\nGoodbye!\n")
            break
        except Exception as e:
            # Handle unexpected errors
            display_message(f"An unexpected error occurred: {str(e)}", is_error=True)


if __name__ == "__main__":
    main()
