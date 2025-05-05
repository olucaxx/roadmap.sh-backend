import requests

def fetch_user_activity(username: str) -> dict:
    """A function to fetch the recent activity from a given user.
    
    Args:
        username (str): the username to get the recent activity

    Raises:
        Exception: if the status code is different from 200

    Returns:
        dict: a dictionary containing the api response
    """
    
    response: requests.Response = requests.get(f"https://api.github.com/users/{username}/events")

    status_code: int = response.status_code

    if status_code != 200: # 200 é o OK, se for diferente é pq deu problema
        raise Exception(status_code)
        
    return response.json()
