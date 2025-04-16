"""
tästä käynnistetään ohjelma
tee valikko: view tasks, New task, edit task,
dit tasks state, delete task, list of task, exit
"""
from task import Task
class Application:

    def main_menu(self, task):
        while True:
            print("Application Menu:")
            print("1. View tasks")
            print("2. New task")
            print("3. Edit task")
            print("4. Edit task state")
            print("5. Delete task")
            print("6. List of tasks")
            print("0. Exit")
            choice = input("Please select an option (1-7): ")
            if choice == '1':
                task.search_tasks()
            elif choice == '2':
                task.new_task()
            elif choice == '3':
                task.edit_task()
            elif choice == '4':
                task.edit_tasks_state()
            elif choice == '5':
                task.delete_task()
            elif choice == '6':
                task.list_of_tasks()
            elif choice == '0':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    task = Task()
    app = Application()
    app.main_menu(task)
    
