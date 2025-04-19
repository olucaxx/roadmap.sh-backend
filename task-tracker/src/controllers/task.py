from src.models import Task, InvalidStatus, InvalidDescription
from src.data import load_tasks, save_tasks

def add_task(description: str) -> str:
    tasks = load_tasks()
    Task.current_id = tasks['current_task_id']
    tasks['tasks'].append(vars(Task(description)))
    tasks['current_task_id'] = Task.current_id
    save_tasks(tasks)
    return f"Task added successfully (ID: {Task.current_id - 1})"

    
def update_task_description(new_description: str, task_id: int) -> str:
    tasks = load_tasks()
    try:
        for task in tasks['tasks']:
            if task['id'] == int(task_id):
                task_obj = Task.from_dict(task)
                task_obj.update_description(new_description.strip())
                task.update(vars(task_obj))
        save_tasks(tasks)
        return f"Task ({task_id}) was updated!"
    
    except InvalidDescription:
        return f"'{new_description}' is not a valid description."

    except ValueError:
        return f"'{task_id}' is not a valid ID."
    

def update_task_status(new_status: int, task_id: int) -> str:
    tasks = load_tasks()
    try:
        for task in tasks['tasks']:
            if task['id'] == int(task_id):
                task_obj = Task.from_dict(task)
                task_obj.update_status(new_status)
                task.update(vars(task_obj))
        save_tasks(tasks)
        return f"Task ({task_id}) was updated!"
    
    except InvalidStatus:
        return f"{new_status} is not a valid status."

    except ValueError:
        return f"'{task_id}' is not a valid ID."


def delete_task(task_id: int) -> str:
    tasks = load_tasks()
    try:
        for task in tasks['tasks']:
            if task['id'] == int(task_id):
                del task
                save_tasks(tasks)
                return f"Task ({task_id}) was deleted!"
            
        return f"Couldn't find a task with id ({task_id})."
    
    except ValueError:
        return f"'{task_id}' is not a valid ID."


def list_all_tasks() -> list[str]:
    tasks = load_tasks()
    result = []
    for task in tasks['tasks']:
        result.append(str(Task.from_dict(task)))
    return result


def list_tasks_by_status(status: int) -> list[str]:
    tasks = load_tasks()
    result = []
    for task in tasks['tasks']:
        if task['status'] == status:
            task_obj = Task.from_dict(task)
            result.append(str(task_obj))
    return result


def reset_tasks() -> None:
    save_tasks({"current_task_id":1, "tasks":[]})
    return "All tasks were deleted and ID was reset to (1)."
