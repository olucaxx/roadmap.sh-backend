def show_user_activity(events: list) -> None:
    if not events:
        print("No recent activities.")
        
    for event in events:
        print(event)
        