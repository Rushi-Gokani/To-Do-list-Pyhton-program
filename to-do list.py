
# List to store tasks
to_do_list = []

# Function to display all tasks
def display_tasks():
    if not to_do_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour to-do list:")
        for idx, task in enumerate(to_do_list, start=1):
            status = '✔️ Completed' if task['completed'] else '❌ Pending'
            print(f"{idx}. {task['name']} - {status}")

# Function to add a task to the list
def add_task():
    task_name = input("\nEnter the task name: ")
    to_do_list.append({'name': task_name, 'completed': False})
    print(f"'{task_name}' has been added to your to-do list.")

# Function to remove a task from the list
def remove_task():
    display_tasks()
    if to_do_list:
        try:
            task_number = int(input("\nEnter the task number to remove: "))
            removed_task = to_do_list.pop(task_number - 1)
            print(f"'{removed_task['name']}' has been removed from your to-do list.")
        except (IndexError, ValueError):
            print("Invalid task number!")

# Function to mark a task as completed/pending
def update_task_status():
    display_tasks()
    if to_do_list:
        try:
            task_number = int(input("\nEnter the task number to mark as completed/pending: "))
            task = to_do_list[task_number - 1]
            task['completed'] = not task['completed']
            status = 'completed' if task['completed'] else 'pending'
            print(f"'{task['name']}' has been marked as {status}.")
        except (IndexError, ValueError):
            print("Invalid task number!")

# Main loop to keep the program running
def to_do_list_app():
    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as completed/pending")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            update_task_status()
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Run the to-do list application
to_do_list_app()
