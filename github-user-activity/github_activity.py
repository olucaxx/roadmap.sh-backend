import argparse
import display
import api_client
from event import *

def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Shows the recent activity from a GitHub user.")
    parser.add_argument('username', type=str, help="The desired username.")

    args: argparse.Namespace = parser.parse_args()
    
    try:
        api_response: dict = api_client.fetch_user_activity(args.username)
        
        events = list()
        for event in api_response:
            match event['type']:
                case "PushEvent":
                    push_event = PushEvent(event["repo"]["id"], event["repo"]["name"], event["payload"]["size"])
                    exists = False
                    
                    for i in events:
                        if i == push_event:
                            i.increment_commits(push_event.commits)
                            exists = True
                    
                    if not exists:
                        events.append(push_event)
                        
                case "CreateEvent":
                    events.append(CreateEvent(event["repo"]["id"], event["repo"]["name"], event["payload"]["ref_type"], 
                                              event["payload"]["ref"] if event["payload"]["ref"] else event["payload"]["master_branch"], ))
                case _:
                    events.append(GenericEvent(event["repo"]["id"], event["repo"]["name"], event["type"]))
                    
        for event in events:
            print(event)
        """ display.user_activity(api_response) """
    except Exception as e:
        print("Error", e)
    
if __name__ == "__main__":
    main()