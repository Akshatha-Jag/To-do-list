# Initialize an empty list to store tasks
todo_list = []


def menu():
    """Display the main menu."""
    while True:
        print("***** Main Menu *****")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting the application.")
            exit()
        else:
            print("Invalid choice. Please try again.")


def add_task():
    """Add a new task to the todo list."""
    task = input("Enter the task: ")
    todo_list.append({"task": task, "status": "pending"})
    print("New task added successfully.\n")


def view_tasks():
    """View all tasks in the todo list."""
    print("Your Todo List:")
    if len(todo_list) == 0:
        print("No pending tasks.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task['task']} - {task['status']}")
    print("\n")


def remove_task():
    """Remove a task from the todo list."""
    if len(todo_list) == 0:
        print("List is empty. No tasks to remove.\n")
        return
    
    try:
        search_index = int(input("Enter the task number that you want to remove: ")) - 1
        if 0 <= search_index < len(todo_list):
            removed_task = todo_list.pop(search_index)
            print(f"Task removed: {removed_task['task']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid task number.\n")


def mark_done():
    """Mark a task as completed."""
    if len(todo_list) == 0:
        print("List is empty. No tasks to mark as done.\n")
        return
    
    try:
        search_index = int(input("Enter the task number that you want to mark as complete: ")) - 1
        if 0 <= search_index < len(todo_list):
            todo_list[search_index]["status"] = "done"
            print(f"Task '{todo_list[search_index]['task']}' has been marked as done.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid task number.\n")


# Start the application
menu()
