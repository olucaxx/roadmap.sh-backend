import requests

def main() -> None:
    username: str = input("username: ").strip()

    response: requests.Response = requests.get(f"https://api.github.com/users/{username}/events")

    status_code: int = response.status_code

    if status_code != 200: # 200 é o OK, se for diferente é pq deu problema
        print("error", status_code)
        return
        
    for event in response.json():
        print(f"{event["type"]} -> {event["repo"]["name"]} | {event["repo"]["id"]}")
    
if __name__ == "__main__":
    main()
