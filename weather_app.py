FILE = "tasks.txt"

def add_task():
    task = input("Enter new task: ")
    with open(FILE, "a") as f:
        f.write(f"[ ] {task}\n")
    print("Task added!\n")

def view_tasks():
    try:
        with open(FILE, "r") as f:
            tasks = f.readlines()
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found.\n")

def complete_task():
    view_tasks()
    num = int(input("Enter task number to mark complete: "))
    with open(FILE, "r") as f:
        tasks = f.readlines()
    if 0 < num <= len(tasks):
        tasks[num-1] = tasks[num-1].replace("[ ]", "[✔]")
        with open(FILE, "w") as f:
            f.writelines(tasks)
        print("Task marked complete!\n")
    else:
        print("Invalid number.\n")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice.\n")