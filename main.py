from task_manager import add_task, list_tasks, mark_done

def show_menu():
    print("\n=== Task Tracker ===")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ").strip()

    if choice == "1":
        task = input("Enter task name: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        try:
            index = int(input("Enter task number to mark as done: ")) - 1
            mark_done(index)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
