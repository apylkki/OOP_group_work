"""
This module defines a Task class that represents a task with attributes such as title, description, deadline, state, and task ID.
It provides getter and setter methods for each attribute, allowing for encapsulation and data management.
"""

class Task:
    def __init__(self, task_id: int, title: str, description: str, deadline: str, state: str):
        self.__task_id = task_id
        self.__title = title
        self.__description = description
        self.__deadline = deadline
        self.__state = state
        self.tasks = []

    # getter and setter methods for each attribute
    @property
    def title(self) -> str:
        return self.__title
    
    @title.setter
    def title(self, title: str):
        self.__title = title
    
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description
    
    @property
    def deadline(self) -> str:
        return self.__deadline
    
    @deadline.setter
    def deadline(self, deadline: str):
        self.__deadline = deadline

    @property
    def state(self) -> str:
        return self.__state
    
    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def task_id(self) -> int:
        return self.__task_id
    
    @task_id.setter
    def task_id(self, task_id: int):
        self.__task_id = task_id
