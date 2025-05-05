class Event():
    repo_id: int
    repo_name: str
    
    def __init__(self, repo_id: int, repo_name: str):
        self.repo_id = repo_id
        self.repo_name = repo_name
        
    def __eq__(self, other):
        return self.repo_id == other.repo_id
        
class CreateEvent(Event):
    ref_type: str
    ref: str | None
    
    def __init__(self, repo_id: int, repo_name: str, ref_type: str, ref: str | None):
        super().__init__(repo_id, repo_name)
        self.ref_type = ref_type
        self.ref = ref
        
    def __str__(self):
        if self.ref_type == "repository":
            return f"Created {self.repo_name} with '{self.ref}' as the master branch"
        return f"Created '{self.ref}' branch in {self.repo_name}"

class PushEvent(Event):
    commits: int
    
    def __init__(self, repo_id: int, repo_name: str, commits: int):
        super().__init__(repo_id, repo_name)
        self.commits = commits
        
    def increment_commits(self, amount: int) -> None:
        self.commits += amount
        
    def __str__(self):
        return f"Pushed {self.commits} {"commits" if self.commits > 1 else "commit"} to {self.repo_name}"

class GenericEvent(Event):
    type: str
    
    def __init__(self, repo_id: int, repo_name: str, type: str):
        super().__init__(repo_id, repo_name)
        self.type = type
        
    def __str__(self):
        return f"GenericEvent({self.repo_id} | {self.repo_name} | {self.type})"
        
if __name__ == "__main__":
    """ push_event = PushEvent(969184548, "olucaxx/roadmap.sh-backend")
    push_event.increment_commits(3)
    
    print(push_event.size) """
    
    