from src.services import *

def main(args: list) -> None:
    if len(args) > 1:
        match args[1]:
            case "help":
                help_command()
                return
            case "add":
                add_task(args[2:])
                return
            case "update":
                update_task(args[2:])
                return
            case "delete":
                delete_task(args[2:])
                return
            case "list":
                list_tasks(args[2:])
                return
            case "mark-in-progress":
                mark_in_progress(args[2:])
                return
            case "mark-done":
                mark_done(args[2:])
                return
            case "reset-tasks":
                reset_tasks()
                return
            case _:
                print("Command not found. Type 'task-cli.py help' to show available commands.")
                return

    print("Type 'task-cli.py help' for information about the script.")
    