import requests

from requests import RequestException

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

    response.raise_for_status()
        
    return response.json()
