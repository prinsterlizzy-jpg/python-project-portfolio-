# todo_list.py
import os
TASK_FILE = "tasks.txt"
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
def add_task(tasks):
    task = input("\nEnter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!")
def remove_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("\nEnter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed}' removed.")
        else:
            print("Invalid number!")
    except ValueError:
        print("Enter a valid number!")
def main():
    tasks = load_tasks()
    while True:
        print("\n==== To-Do List Menu ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("👋 Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid choice! Try again.")
if __name__ == "__main__":
    main()