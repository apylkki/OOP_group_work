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
                task_id = int(input("Enter task ID to shearch (0 to exit): "))
                if task_id in self.tasks:
                    task = self.tasks[task_id]
                    print(f"Task: {task.title}, {task.description}, {task.deadline}, {task.state}")
                    return task
                elif task_id == 0:
                    print("Exiting search.")
                    break
                else:
                    print("Task not found. Please try again.\n")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.\n")

    def new_task(self): 
        """Create a new task"""
        task_id = len(self.tasks) + 1 # Automated task ID generation
        title = input("Enter title for new task: ")
        description = input("Enter the description for task: ")
        deadline = input("Enter the deadline for task: ")
        
        task = Task(task_id, title, description, deadline, "new")
        self.tasks[task_id] = task
        
        print(f"Task {task_id} created: Title: {task.title}, Description: {task.description}, Deadline: {task.deadline}, State: {task.state}")
        return task

    def edit_task(self): #heidi
        """Edit an existing task."""
        if not self.tasks:
            print("No tasks available to edit.")
            return
        try:
            task_id = int(input("Enter task ID to edit: "))
            if task_id in self.tasks:
                task = self.tasks[task_id]
                print(f"Editing task: {task.title}, {task.description}, {task.deadline}, {task.state}")

                new_title = input(f"Enter new title: ")
                new_description = input(f"Enter new description: ")
                new_deadline = input(f"Enter new deadline: ")
                new_state = input(f"Enter new state: ")

                if new_title:
                    task.title = new_title
                if new_description:
                    task.description = new_description
                if new_deadline:
                    task.deadline = new_deadline
                if new_state:
                    task.state = new_state
                print(f"Task {task_id} updated: {task.title}, {task.description}, {task.deadline}, {task.state}")
                return task
            else:
                print("Task not found.")
                return None
        except ValueError:
            print("Invalid input. Please enter a valid task ID.")
            return None

    def edit_tasks_state(self): #heidi
        """Edit the state of an existing task."""
        if not self.tasks:
            print("No tasks available to edit.")
            return
        try:
            task_id = int(input("Enter task ID to edit state: "))
            if task_id in self.tasks:
                task = self.tasks[task_id]
                print(f"Editing task state: {task.title}, {task.description}, {task.deadline}, {task.state}")

                new_state = input(f"Enter new state (new, work in progress, finished): ").strip().lower()
                if new_state in ["new", "work in progress", "finished"]:
                    task.state = new_state
                    print(f"Task {task_id} updated state to: {task.state}")
                else:
                    print("Invalid state. Please enter a valid state.")
        except ValueError:
            print("Invalid input. Please enter a valid task ID.")
            return None

    def delete_task(self):
        """Delete an existing task."""
        if not self.tasks:
            print("No tasks available to delete.")
            return
        while True:
            try:
                task_id = int(input("Enter task ID to delete (or 0 to cancel): "))
                if task_id == 0:
                    print("Delete operation canceled.")
                    return
                
                if task_id in self.tasks:
                    task = self.tasks[task_id]
                    del self.tasks[task_id]
                    print(f"Task deleted: {task.title}, {task.description}, {task.deadline}, {task.state}")
                elif task_id not in self.tasks:
                    print("Task not found. Please enter a valid task ID.")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
                return
                

    def list_of_tasks(self):
        """Displays all the tasks."""
        
        if not self.tasks:
            print("No tasks available. Task list is empty.")
            return
        
        print("All tasks: ")
        for task_id, task in self.tasks.items():
            print(f"ID: {task_id}, Title: {task.title}, Description: {task.description}, Deadline: {task.deadline}, State: {task.state}")
        return
    
        