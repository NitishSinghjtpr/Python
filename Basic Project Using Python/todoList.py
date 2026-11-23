import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


tasks = load_tasks()


# Save tasks in file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Add Task
def add_task():
    task = input("Enter your task: ")

    tasks.append({
        "task": task,
        "completed": False
    })

    save_tasks()
    print("Task added successfully!")


# View Tasks
def view_tasks():
    if not tasks:
        print("No tasks available!")
        return

    print("\n===== YOUR TASKS =====")

    for i, task in enumerate(tasks, start=1):

        status = "Completed" if task["completed"] else "Pending"

        print(f"{i}. {task['task']} [{status}]")


# Delete Task
def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_no = int(input("Enter task number to delete: "))

        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)

            save_tasks()

            print(f"{removed['task']} deleted successfully!")

        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


# Update Task
def update_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_no = int(input("Enter task number to update: "))

        if 1 <= task_no <= len(tasks):

            new_task = input("Enter new task: ")

            tasks[task_no - 1]["task"] = new_task

            save_tasks()

            print("Task updated successfully!")

        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


# Mark Task Completed
def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_no = int(input("Enter task number to complete: "))

        if 1 <= task_no <= len(tasks):

            tasks[task_no - 1]["completed"] = True

            save_tasks()

            print("Task marked as completed!")

        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


# Search Task
def search_task():
    search = input("Enter task name to search: ").lower()

    found = False

    for i, task in enumerate(tasks, start=1):

        if search in task["task"].lower():

            print(f"{i}. {task['task']}")
            found = True

    if not found:
        print("Task not found!")


# Total Task Count
def total_tasks():
    total = len(tasks)

    completed = sum(1 for task in tasks if task["completed"])

    pending = total - completed

    print("\n===== TASK SUMMARY =====")
    print("Total Tasks:", total)
    print("Completed Tasks:", completed)
    print("Pending Tasks:", pending)


# Main Menu
while True:

    print("\n========== TO-DO LIST ==========")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Mark Task Completed")
    print("6. Search Task")
    print("7. Total Tasks Count")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        update_task()

    elif choice == "5":
        complete_task()

    elif choice == "6":
        search_task()

    elif choice == "7":
        total_tasks()

    elif choice == "8":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice! Please try again.")