tasks=[] 

def add_tasks():
    task=input("Enter the task:")
    priority = input("priority (high/medium/low): ").lower()
    tasks.append({"task": task, "priority": priority, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks!")
        return
    print("\nTo-Do List:")
    for i, t in enumerate(tasks, 1):
        status = "✓" if t["done"] else "o"
        print(f"{i}. [{t['priority'].title()}] {status} {t['task']}")

def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        idx = int(input("Mark done (number): ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print('market done!')
        else:
            print("Invalid number!")
    except ValueError:
        print("enter number")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        idx = int(input("Delete (number): ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Enter number!")

print("Welcome to the Task manager!")
while True:
    print("--Task manager mEnu--")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Done")
    print("4. delete Task")
    print("0. Exit")

    choice=input("Enter your choice:")
    if choice=='1':
        add_tasks()
    elif choice=='2':
        view_tasks()
    elif choice=='3':
        mark_done()
    elif choice=='4':
        delete_task()
    elif choice=='0':
        break
    else:
        print("Invalid")

