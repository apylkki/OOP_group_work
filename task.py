"""
view tasks 
New task
edit task
edit tasks state
delete task
list of task
"""

class Task:
    def __init__(self):
        self.tasks = []
        self.task_id = 0

    def view_tasks(self):
        print("View tasks")

    def new_task(self):
        print("New task")

    def edit_task(self):
        print("Edit task")

    def edit_tasks_state(self):
        print("Edit tasks state")

    def delete_task(self):
        print("Delete task")

    def list_of_tasks(self):
        print("List of tasks")

