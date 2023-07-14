# To-Do List App

import csv

class TodoList:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = []

    def load_tasks(self):
        with open(self.file_path, 'r') as file:
            csv_reader = csv.reader(file)
            self.tasks = [row[0] for row in csv_reader]

    def save_tasks(self):
        with open(self.file_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            for task in self.tasks:
                csv_writer.writerow([task])

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.save_tasks()
            print("Task removed successfully!")
        else:
            print("Task not found!")

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks found!")

# Test the To-Do List App
file_path = 'tasks.csv'
todo_list = TodoList(file_path)
todo_list.load_tasks()

print("1. Add task")
print("2. Remove task")
print("3. View tasks")
print("4. Exit")

while True:
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        task = input("Enter the task: ")
        todo_list.add_task(task)
    elif choice == 2:
        task = input("Enter the task to remove: ")
        todo_list.remove_task(task)
    elif choice == 3:
        todo_list.view_tasks()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")


'''
=================================
Test Case:
=================================

1. Add task
2. Remove task
3. View tasks
4. Exit
Enter your choice (1-4): 3
Tasks:
1. Task
2. Complete assignment
3. Go grocery shopping
4. Walk the dog
5. Clean the house
Enter your choice (1-4): 2
Enter the task to remove: Walk the dog
Task removed successfully!
Enter your choice (1-4): 3
Tasks:
1. Task
2. Complete assignment
3. Go grocery shopping
4. Clean the house
Enter your choice (1-4): 2
Enter the task to remove: task
Task not found!
Enter your choice (1-4): 2
Enter the task to remove: Task

'''