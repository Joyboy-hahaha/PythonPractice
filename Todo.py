# TO DO list

import os

filename = 'todo.txt'

def loadTask():
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        return []

def saveTask(tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f'{task}\n')

def showTask(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f'{i}. {task}')

tasks = loadTask()

while True:
    print('----TO DO List----')
    print('1. Add Task')
    print('2. Show Task')
    print('3. Delete Task')
    print('4. Quit')

    try:
        choice = int(input('Enter your choice (1-4): '))
        if choice == 1:
            add_task = input('Enter a task: ').strip()
            if add_task:
                tasks.append(add_task)
                saveTask(tasks)
                print('Task added successfully')
            else:
                print('task cannot be empty')
                continue
        elif choice == 2:
            if tasks:
                showTask(tasks)
            else:
                print('Task is Empty')
        elif choice == 3:
            if tasks:
                showTask(tasks)
                try:
                    user_delete = int(input('Enter a number to delete: '))
                    if user_delete>=1 and user_delete<=len(tasks):
                        removed = tasks.pop(user_delete - 1)
                        print(f'Deleted: {removed}')
                        saveTask(tasks)
                        print('Deleted success')
                    else:
                        print('Please enter a valid number.')
                except ValueError:
                    print('Enter a valid value')
        elif choice == 4:
            print('GoodBye')
            break

    except ValueError:
        print('Enter a valid number.')