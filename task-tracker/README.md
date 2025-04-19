# CLI TASK MANAGER
## Introduction
CLI Task Manager is a simple task manager that runs on the terminal. The tasks are stored in a JSON file (tasks.json), where each task has an ID, description, and status. It offers operations such as add tasks, update status, update description, delete tasks, list tasks, etc.

It was made to practice essential python skills and technologies, such as the `json` module, `args` handling, custom exceptions, error handling and much more.

It was made following the instructions of the project [`task-tracker`](https://roadmap.sh/projects/task-tracker), from the famous Roadmap.sh

The instruction "Do not use any external libraries or frameworks to build this project." makes the project more challenging. I would have used `setuptools` in a usual scenario, but I wanted to stick with the project's guidelines, so you have to use `python task-cli.py ...` in order to run the code. 

If you wish to know more, the project instructions can be accessed by clicking [here](https://roadmap.sh/projects/task-tracker).

## Requirements
- Python 3.10 or superior installed.
- **No additional Python packages are required to run the project.**

## Installation and execution
First, you must clone the repo and go into the `task-cli` folder
```sh
git clone https://github.com/olucaxx/task-cli
cd task-cli
```
Inside the repository you can use `python task-cli.py [command] [args]` in order to manage your tasks.

### Available commands
```
help                      Shows a help page of how to use the code.
add "DESCRIPTION"         Add a new task with the given description.
update ID "DESCRIPTION"   Update the description of the task with the given ID.
delete ID                 Delete the task with the specified ID.
mark-in-progress ID       Mark the task with the given ID as "in progress".
mark-done ID              Mark the task with the given ID as "done".
list                      List all tasks.
list [STATUS]             List tasks filtered by status (todo, in-progress, done).
reset-tasks               Remove all tasks and reset task IDs.
```
### Available arguments
```
ID      A unique number assigned to each task, used to identify and manage tasks.
STATUS  The current state of a task. Can be one of the following:
        - todo: The task is yet to be started.
        - in-progress: The task is currently being worked on.
        - done: The task has been completed.
```
### Example
```
$ python task-cli.py add "Finish the report"
Task added successfully (ID: 1)

$ python task-cli.py list
01 | Finish the report         | todo        | 07/03/2025 06:51:41 | 07/03/2025 06:51:41

$ python task-cli.py update 1 "Finish the report and review"
Task (1) was updated!

$ python task-cli.py mark-done 1
Task (1) was updated!

$ python task-cli.py list
01 | Finish the report and rev | done        | 07/03/2025 06:51:41 | 07/03/2025 06:52:30
```
