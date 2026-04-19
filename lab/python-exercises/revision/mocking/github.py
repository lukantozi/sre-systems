import requests

def get_user_info(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code != 200:
        return None
    data = response.json()
    return {
        "name": data["name"],
        "repos": data["public_repos"],
        "followers": data["followers"]
    }
