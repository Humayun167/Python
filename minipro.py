import json


def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)


def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = 'Done' if task['completed'] else 'Not Done'
            print(f"{index}. {task['description']} - {status}")


def add_task(tasks, description):
    task = {'description': description, 'completed': False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{description}' added successfully.")


def mark_completed(tasks, index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task index.")


def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        save_tasks(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task index.")


def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List:")
        display_tasks(tasks)

        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == '2':
            index = int(input("Enter the task index to mark as completed: "))
            mark_completed(tasks, index)
        elif choice == '3':
            index = int(input("Enter the task index to delete: "))
            delete_task(tasks, index)
        elif choice == '4':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
