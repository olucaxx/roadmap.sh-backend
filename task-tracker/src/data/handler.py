import json
from json import JSONDecodeError

file_path = "src/data/tasks.json"

def load_tasks() -> dict:
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)
            
    except FileNotFoundError: # arquivo não encontrado
        json_data = {"current_task_id":1, "tasks":[]}
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, indent=4)
            
    except JSONDecodeError: # arquivo vazio
        json_data = {"current_task_id":1, "tasks":[]}
        
    return json_data

def save_tasks(json_data: dict) -> None:
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)
        