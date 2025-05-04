import argparse
import display
import api_client

def main() -> None:
    parser = argparse.ArgumentParser(description="Shows the recent activity from a GitHub user.")
    parser.add_argument('username', type=str, help="The desired username.")

    args = parser.parse_args()
    
    try:
        api_response: dict = api_client.fetch_user_activity(args.username)
        display.user_activity(api_response)
    except Exception as e:
        print("Error", e)
    
if __name__ == "__main__":
    main()