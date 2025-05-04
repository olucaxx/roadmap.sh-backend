import requests

def fetch_user_activity(username: str) -> dict:
    response: requests.Response = requests.get(f"https://api.github.com/users/{username}/events")

    status_code: int = response.status_code

    if status_code != 200: # 200 é o OK, se for diferente é pq deu problema
        raise Exception(status_code)
        
    return response.json()
