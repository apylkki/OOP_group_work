"""
TaskManager class for managing tasks in a task management system.
This class provides methods to search, create, edit, delete, and list tasks.
"""
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []  # List to store tasks

    def search_tasks(self): #heidi
        # Implement search functionality here
        task_id = int(input("Enter task ID to shearch: "))
        for task in self.tasks:
            if task.get_task_id() == task_id:
                print(f"Task found: {task.get_title()}, {task.get_description()}, {task.get_deadline()}, {task.get_state()}")
                return task
        print("Task not found.")

    def new_task(self): #säde
        # automatisoi task_id luonti
        print("New task")

    def edit_task(self): #heidi, haku id mukaan
        print("Edit task")

    def edit_tasks_state(self): #heidi, id mukaan, new, work in progress, finished, also possibly pending, delayed, backburner 
        print("Edit tasks state")

    def delete_task(self): #säde
        print("Delete task")

    def list_of_tasks(self): #säde
        print("List of tasks")