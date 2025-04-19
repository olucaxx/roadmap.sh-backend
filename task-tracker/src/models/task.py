from datetime import datetime

class InvalidDescription(Exception):
    pass

class InvalidStatus(Exception):
    pass

class Task:
    current_id: int = 1
    STATUS_MAP = {0: "todo", 1: "in-progress", 2: "done"}
    
    def __init__(self, description: str, task_id: int = None, status: int = 0, created_at: str = None, updated_at: str = None):
        self.id: int = int(task_id) if task_id is not None else Task.current_id
        self.description: str = description
        self.status: int = status
        self.created_at: str = created_at if created_at else Task.get_current_datetime()
        self.updated_at: str = updated_at if updated_at else Task.get_current_datetime()

        if task_id is None:
            Task.current_id += 1
    
    
    def update_description(self, new_description: str) -> None:
        if not new_description or not new_description.strip():
            raise InvalidDescription
        
        self.description = new_description
        self.updated_at = Task.get_current_datetime()
    
    
    def update_status(self, new_status: int) -> None:
        if new_status not in self.STATUS_MAP:
            raise InvalidStatus
        
        self.status = new_status
        self.updated_at = Task.get_current_datetime()
       
       
    def get_status_label(self) -> str:
        return self.STATUS_MAP[self.status]
        
    @staticmethod    
    def get_current_datetime() -> str:
        return datetime.now().strftime('%d/%m/%Y %H:%M:%S')    
        
    
    @classmethod
    def from_dict(cls, task_data: dict):
        return cls(
            description = task_data['description'],
            task_id = task_data['id'],
            status = task_data['status'],
            created_at = task_data['created_at'],
            updated_at = task_data['updated_at']
        )
        
    def __str__(self):
        return f"{self.id:02} | {self.description[:25]:25} | {self.get_status_label():11} | {self.created_at} | {self.updated_at}"
