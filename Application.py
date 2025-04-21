"""
This is the main file of the application, where the main menu is created and the program is started.
"""
from task import Task
from taskmanager import TaskManager

class Application:
    def main_menu(self, task_manager: TaskManager):
        while True:
            print("\nApplication Menu:")
            print("0. Exit")
            print("1. Search tasks")
            print("2. New task")
            print("3. Edit task")
            print("4. Edit task state")
            print("5. Delete task")
            print("6. List of tasks")
            choice = input("\nPlease select an option (0-6): ")
            if choice == '0':
                print("\nThank you for using Task Manager!")
                break
            elif choice == '1':
                task_manager.search_tasks()
            elif choice == '2':
                task_manager.new_task()
            elif choice == '3':
                task_manager.edit_task()
            elif choice == '4':
                task_manager.edit_tasks_state()
            elif choice == '5':
                task_manager.delete_task()
            elif choice == '6':
                task_manager.list_of_tasks()
            else:
                print("Invalid choice. Please try again.")

#Test
"""
def test(task_manager):
    task1 = Task("Task 1", "Homework", "30-04-2025", "new", 1)
    task2 = Task("Task 2", "Group work", "26-4-2025", "work in progress", 2)
    task3 = Task("Task 3", "Group meeting", "05-4-2025", "finished", 3)

    task_manager.tasks.append(task1)
    task_manager.tasks.append(task2)
    task_manager.tasks.append(task3)
"""

if __name__ == "__main__":
    task_manager = TaskManager()
    app = Application()

    #test chearch_tasks-mehtod
    #test(task_manager)

    #start the application
    app.main_menu(task_manager)
    
