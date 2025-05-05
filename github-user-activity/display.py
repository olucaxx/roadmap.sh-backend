def user_activity(response: dict) -> None:
    """_summary_

    Args:
        response (dict): _description_
    """
    if not response:
        print("No recent activities.")
        
    for event in response:
        print(f"{event["type"]} -> {event["repo"]["name"]} | {event["repo"]["id"]}")
        