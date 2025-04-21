"""
TaskManager class for managing tasks in a task management system.
This class provides methods to search, create, edit, delete, and list tasks.
"""
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = {}  # Dictionary to store tasks

    def search_tasks(self): #heidi
        """Search for a task by its ID."""
        if not self.tasks:
            print("Task not found. No tasks have been created yet.\n")
            return
        while True:
            try:
                task_id = int(input("Enter task ID to shearch: "))
                if task_id == self.tasks:
                    task = self.tasks[task_id]
                    print(f"Task: {task.title}, {task.description}, {task.deadline}, {task.state}")
                    return task
                else:
                    print("Task not found. Please try again.\n")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.\n")

    def new_task(self): #säde, state on aina new
        # Automated task ID generation
        print("New task")

    def edit_task(self): #heidi, haku id mukaan
        print("Edit task")

    def edit_tasks_state(self): #heidi, id mukaan, new, work in progress, finished, also possibly pending, delayed, backburner 
        #käytä librarya tämän tehtävän tekemiseen
        print("Edit tasks state")

    def delete_task(self): #säde
        print("Delete task")

    def list_of_tasks(self): #säde
        print("List of tasks")