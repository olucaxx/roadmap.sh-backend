import argparse
import display
import api_client
from events import CreateEvent, PushEvent, GenericEvent
from requests.exceptions import ConnectionError, HTTPError, RequestException

def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Shows the recent activity from a given GitHub user.")
    parser.add_argument('username', type=str, help="The account username.")

    args: argparse.Namespace = parser.parse_args()
    
    try:
        api_response: dict = api_client.fetch_user_activity(args.username)
        activities: list = [] # irá armazenar nossas atividades, os eventos retornados
        
        for data in api_response:
            repo_id: int = data["repo"]["id"]
            repo_name: str = data["repo"]["name"]
            
            match data['type']:
                case "PushEvent":
                    event = PushEvent(repo_id, repo_name, data["payload"]["size"])
                    already_exists = False
                    
                    for activity in activities:
                        if activity == event:
                            activity += event.commits # soma a quantidade de commits
                            already_exists = True
                            break
                    
                    if not already_exists:
                        activities.append(event)
                        
                case "CreateEvent":
                    activities.append(CreateEvent(repo_id, repo_name, data["payload"]["ref_type"], data["payload"]["ref"]))
                    
                case _: # caso seja um novo tipo de vento que ainda não tem uma classe definida
                    activities.append(GenericEvent(repo_id, repo_name, data["type"]))
                    
        display.show_user_activity(activities)
    except ConnectionError as e:
        print("A connection error occurred:", e)
    except HTTPError as e:
        print("HTTP Error:", e)
    except RequestException as e:
        print("An error occurred:", e)
    except Exception as e:
        print("Error", e)
    
if __name__ == "__main__":
    main()