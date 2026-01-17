

## 🧑‍💻 Python Implementation (`task_manager.py`)


tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index + 1}. {task['task']} - {status}")

def complete_task():
    view_tasks()
    try:
        task_number = int(input("Enter task number to mark as completed: "))
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    while True:
        print("\n--- Student Task Management System ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")

main()
