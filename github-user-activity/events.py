from abc import ABC, abstractmethod

class Event(ABC):
    repo_id: int
    repo_name: str

    def __init__(self, repo_id: int, repo_name: str) -> None:
        self.repo_id = repo_id
        self.repo_name = repo_name

    @abstractmethod
    def __str__(self) -> str:
        pass
        
class CreateEvent(Event):
    ref_type: str
    ref: str | None
    
    def __init__(self, repo_id: int, repo_name: str, ref_type: str, ref: str | None) -> None:
        super().__init__(repo_id, repo_name)
        self.ref_type = ref_type
        self.ref = ref # isso pode ser None no caso do ref_type ser um 'repository'
        
    def __str__(self) -> str:
        if self.ref_type == "repository":
            return f"Created {self.repo_name}"
        
        return f"Created '{self.ref}' {self.ref_type} in {self.repo_name}"

class PushEvent(Event):
    commits: int
    
    def __init__(self, repo_id: int, repo_name: str, commits: int) -> None:
        super().__init__(repo_id, repo_name)
        self.commits = commits
        
    def __eq__(self, other: "PushEvent") -> bool:
        if isinstance(other, PushEvent):
            return self.repo_id == other.repo_id
        
        return False
        
    def __iadd__(self, amount: int) -> "PushEvent":
        self.commits += amount
        return self
        
    def __str__(self) -> str:
        return f"Pushed {self.commits} {"commits" if self.commits > 1 else "commit"} to {self.repo_name}"

class GenericEvent(Event):
    type: str
    
    def __init__(self, repo_id: int, repo_name: str, type: str) -> None:
        super().__init__(repo_id, repo_name)
        self.type = type
        
    def __str__(self) -> str:
        return f"GenericEvent({self.repo_id} | {self.repo_name} | {self.type})"
    