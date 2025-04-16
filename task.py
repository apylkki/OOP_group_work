"""
view tasks 
New task
edit task
edit tasks state
delete task
list of task
"""

class Task:

    # automatisoi id luonti
    def __init__(self):
        self.tasks = []
        self.task_id = 0

    def search_tasks(self): #heidi, etsi id mukaan
        print("View tasks")

    def new_task(self): #säde
        print("New task")

    def edit_task(self): #heidi
        print("Edit task")

    def edit_tasks_state(self): #heidi
        print("Edit tasks state")

    def delete_task(self): #säde
        print("Delete task")

    def list_of_tasks(self): #säde
        print("List of tasks")

