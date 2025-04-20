"""
This module defines a Task class that represents a task with attributes such as title, description, deadline, state, and task ID.
It provides getter and setter methods for each attribute, allowing for encapsulation and data management.
"""

class Task:
    def __init__(self, title: str, description: str, deadline: str, state: str, task_id: int):
        self.__title = title
        self.__description = description
        self.__deadline = deadline
        self.__state = state
        self.__task_id = task_id
        self.tasks = []

    # getter methods
    def get_title(self):
        return self.__title
    
    def get_description(self):
        return self.__description
    
    def get_deadline(self):
        return self.__deadline
    
    def get_state(self):
        return self.__state
    
    def get_task_id(self):
        return self.__task_id
    
    # setter methods
    def set_title(self, title):
        self.__title = title

    def set_description(self, description):
        self.__description = description

    def set_deadline(self, deadline):
        self.__deadline = deadline

    def set_state(self, state):
        self.__state = state

    def set_task_id(self, task_id):
        self.__task_id = task_id

