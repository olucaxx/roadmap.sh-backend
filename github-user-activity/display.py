def user_activity(response: dict):
    if not response:
        print("No recent activities.")
    for event in response:
        print(f"{event["type"]} -> {event["repo"]["name"]} | {event["repo"]["id"]}")
        