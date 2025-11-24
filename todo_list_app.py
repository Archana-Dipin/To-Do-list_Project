# version 1.0 of todo list without any ui , database or file storage, user login, just basic todo list functionality.
from datetime import date
list_of_todos = []

def add_todo_item() -> None:
    while True:
        item = input(f"Enter your tasks [Enter 'q' to stop adding task] -- \n")
        if item.lower() == 'q':
            break
        else:
            list_of_todos.append(item)
            # print(f'"{item}" added successfully.\n')

def remove_item_from_todo_list() -> None:
    if not list_of_todos:
        print("No tasks to remove, add a task\n")
        return
    display_todo_list()
    while True:
        option = input(f"Enter the number of the task you would like to delete.[Enter 'q' to stop deleting]").strip()
        if option.lower() == 'q':
            break
        if option.isdigit():
            index = int(option) - 1
            if 0 <= index < len(list_of_todos):
                print(f"Removed task is - {list_of_todos.pop(index)}")
            else:
                print(f"Enter a valid number to remove the task\n")
                return
        else:
            print(f"Enter a valid value\n")
def display_todo_list() -> None:
    print(f"{"-" * 30}\nList of {date.today()} tasks \n{"-" * 30}\n")
    if list_of_todos:
        for index, agenda in enumerate(list_of_todos, start=1):
            print(f"{index}. {agenda}\n")
    else:
        print("No tasks to display please add a task\n")

def show_menu():
    print(f"{"="*30} Date - {date.today()} -- Todo List {"="*30}")
    print(f" 1. Add new task\n 2. Remove the task\n 3. Display your tasks\n 4. Exit from To-Do list app \n{"="*92}")
while True:
    show_menu()
    options = int(input("Enter your choice\n"))
    match options:
        case 1 : add_todo_item()
        case 2 : remove_item_from_todo_list()
        case 3 : display_todo_list()
        case 4 : break
        case _ : print("Enter a valid option 1-4\n")

