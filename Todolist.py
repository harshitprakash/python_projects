class TodoApp:
    def __init__(self):
        self.tasks = []  # Store tasks within the instance of the class

    def show_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("\nYour to-do list is empty!")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def add_task(self):
        """Allow the user to add a task."""
        task = input("Enter a task to add to your list: ")
        self.tasks.append(task)  # Add task to the internal tasks list
        print(f"'{task}' has been added to your list.")

    def delete_task(self):
        """Allow the user to delete a task."""
        self.show_tasks()
        try:
            task_number = int(input("\nEnter the number of the task you want to delete: "))
            if 1 <= task_number <= len(self.tasks):
                removed_task = self.tasks.pop(task_number - 1)  # Remove the task
                print(f"'{removed_task}' has been deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def run(self):
        """Run the app and handle user interaction."""
        while True:
            print("\nTo-Do List App")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Delete Task")
            print("4. Exit")
            
            choice = input("Choose an option (1/2/3/4): ")
            
            if choice == '1':
                self.show_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                print("Goodbye! Have a great day!")
                break
            else:
                print("Invalid choice, please try again.")

# Running the app
if __name__ == "__main__":
    todo_app = TodoApp()  # Create an instance of the class
    todo_app.run()  # Run the app
