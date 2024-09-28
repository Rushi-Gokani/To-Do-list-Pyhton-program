# To-Do-list-Pyhton-program
A simple To-Do List Application written in Python, designed to help users manage daily tasks. Users can add, view, remove tasks, and optionally mark tasks as completed or pending.

## Features
### Add Task
Users can add a task to the to-do list. Each task will initially be marked as "pending."

### View Tasks
Users can view all tasks in the list along with their current status (either "Pending" or "Completed").

### Remove Task
Users can remove a task from the list by specifying the task number.

### Mark Task as Completed/Pending
Users can toggle the status of a task (mark it as "completed" or "pending").

### Exit
The program runs continuously until the user chooses to exit.

### How It Works
The application works in a loop where users are presented with a menu of options. They can interact with the to-do list by selecting options to add, view, remove, or update tasks. The list of tasks is displayed with their status.

The tasks are stored as dictionaries inside a list, where each dictionary contains:

name: The name of the task.
completed: The status of the task (either True for "completed" or False for "pending").
Installation & Setup
### Requirements
Python 3.x


### Clone or Download the Repository
You can either clone the repository using Git or download the source files:
git clone <repository-url>

### Run the Application
Open a terminal and navigate to the directory where the Python script is located. Run the following command to start the application:
python to_do_list.py

### Usage
Once the application starts, you will see a menu with the following options:
Options:
1. View tasks
2. Add task
3. Remove task
4. Mark task as completed/pending
5. Exit
Add Task
Select option 2 to add a task. You will be prompted to enter the task name, and it will be added to the list with a "pending" status.

View Tasks
Select option 1 to view all tasks. Each task will be listed with its number and status (either "Completed" or "Pending").

Remove Task
Select option 3 to remove a task by entering its corresponding number.

Mark Task as Completed/Pending
Select option 4 to toggle the status of a task (mark as "completed" or "pending") by entering its corresponding number.

Exit
Select option 5 to exit the application.

### Example Usage
Options:
1. View tasks
2. Add task
3. Remove task
4. Mark task as completed/pending
5. Exit
Choose an option (1-5): 2

Enter the task name: Buy groceries
'Buy groceries' has been added to your to-do list.

Options:
1. View tasks
2. Add task
3. Remove task
4. Mark task as completed/pending
5. Exit
Choose an option (1-5): 1

Your to-do list:
1. Buy groceries - ❌ Pending
License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code as needed.

Acknowledgments
This project was created to practice Python fundamentals, including lists, loops, conditionals, and user input handling. It's a simple but practical exercise for beginners learning Python.
