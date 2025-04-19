import src.controllers.task as controller
from inspect import cleandoc

def add_task(args: list):
    if not args:
        print("You need to give a description for your task.")  
        return
    
    if len(args) >= 2:
        print(f"Too many arguments, expected 1, got {len(args)}.")
        return
    
    print(controller.add_task(args[0]))


def update_task(args: list):
    if not args or len(args) < 2:
        print("You need to type the ID and a new description for your task.")
        return
    
    if len(args) >= 3:
        print(f"Too many arguments, expected 2, got {len(args)}.")
        return

    print(controller.update_task_description(args[1], args[0]))


def delete_task(args: list):
    if not args:
        print("You need to type the ID of your task.")
        return
    
    if len(args) >= 2:
        print(f"Too many arguments, expected 1, got {len(args)}.")
        return

    print(controller.delete_task(int(args[0])))
    

def mark_in_progress(args: list):
    if not args:
        print("You need to type the ID of your task.")
        return
    
    if len(args) >= 2:
        print(f"Too many arguments, expected 1, got {len(args)}.")
        return

    print(controller.update_task_status(1, args[0]))


def mark_done(args: list):
    if not args:
        print("You need to type the ID of your task.")
        return
    
    if len(args) >= 2:
        print(f"Too many arguments, expected 1, got {len(args)}.")
        return

    print(controller.update_task_status(2, args[0]))


def list_tasks(args: list):
    if not args:
        for task in controller.list_all_tasks():
            print(task)
        return
    
    if len(args) >= 2:
        print(f"Too many arguments, expected 1, got {len(args)}.")
        return
    
    match args[0]:        
        case "todo":
            for task in controller.list_tasks_by_status(0):
                print(task)
            return
        
        case "in-progress":
            for task in controller.list_tasks_by_status(1):
                print(task)
            return
        
        case "done":
            for task in controller.list_tasks_by_status(2):
                print(task)
            return
        
        case _:
            print(f"Couldn't resolve \"{args[0]}\".")
            return
    

def reset_tasks():
    print("Are you sure you want to delete all your history? This cannot be undone.")
    confirm = input("If so, please type \"I am sure\": ").strip()
    
    if confirm == "I am sure":
        print(controller.reset_tasks())
        return
    
    print(f"You typed \"{confirm}\", operation cancelled.")
    
    
def help_command():
    print(cleandoc(
        '''
        Usage: 
            task-cli.py [COMMAND] [ARGS]
        
        Commands:
            help                      Shows a help page of how to use the code.
            add "DESCRIPTION"         Add a new task with the given description.
            update ID "DESCRIPTION"   Update the description of the task with the given ID.
            delete ID                 Delete the task with the specified ID.
            mark-in-progress ID       Mark the task with the given ID as "in progress".
            mark-done ID              Mark the task with the given ID as "done".
            list                      List all tasks.
            list [STATUS]             List tasks filtered by status (todo, in-progress, done).
            reset-tasks               Remove all tasks and reset task IDs.

        Arguments:
            ID      A unique number assigned to each task, used to identify and manage tasks.
            STATUS  The current state of a task. Can be one of the following:
                    - todo: The task is yet to be started.
                    - in-progress: The task is currently being worked on.
                    - done: The task has been completed.

        For more information, visit: https://github.com/olucaxx/task-cli
        '''
        ))
    