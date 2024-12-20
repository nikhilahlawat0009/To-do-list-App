import json
import os

# Dynamically determine the directory of the script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# File to store tasks
TASKS_FILE = os.path.join(SCRIPT_DIR, "tasks.json")

# Load tasks from the file or create an empty list
def load_tasks():
    print(f"Loading tasks from: {TASKS_FILE}")
    if not os.path.exists(TASKS_FILE):
        print("File not found. Creating a new task list.")
        return []
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
            print(f"Loaded tasks: {tasks}")
            return tasks
    except json.JSONDecodeError:
        print("Error reading tasks file. Returning an empty task list.")
        return []

# Save tasks to the file
def save_tasks(tasks):
    print(f"Saving tasks to: {TASKS_FILE}")
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
            print("Tasks saved successfully.")
    except Exception as e:
        print(f"Error saving tasks: {e}")

# Add a new task
def add_task(title, priority):
    tasks = load_tasks()
    tasks.append({"title": title, "priority": priority, "completed": False})
    save_tasks(tasks)
    print(f"Task '{title}' added successfully.")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nCurrent Tasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{idx}. {task['title']} - Priority: {task['priority']} - Completed: {status}")

# Mark a task as completed
def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print(f"Task '{tasks[index]['title']}' marked as completed.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{deleted_task['title']}' deleted successfully.")
    else:
        print("Invalid task number.")

# Search for tasks
def search_tasks(query):
    tasks = load_tasks()
    results = [task for task in tasks if query.lower() in task["title"].lower()]
    if results:
        print("\nSearch Results:")
        for idx, task in enumerate(results, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{idx}. {task['title']} - Priority: {task['priority']} - Completed: {status}")
    else:
        print("No tasks found matching your search.")

# Main menu
def menu():
    while True:
        print("\n--- To-Do List App ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. Exit")

        try:
            choice = input("Choose an option: ")
            if choice == "1":
                title = input("Enter task title: ")
                priority = input("Enter task priority (High/Medium/Low): ")
                add_task(title, priority)
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                index = int(input("Enter task number to mark as completed: ")) - 1
                complete_task(index)
            elif choice == "4":
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)
            elif choice == "5":
                query = input("Enter search query: ")
                search_tasks(query)
            elif choice == "6":
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run the app
if __name__ == "__main__":
    try:
        menu()
    except Exception as e:
        print(f"Critical error: {e}")
        input("Press Enter to exit...")
