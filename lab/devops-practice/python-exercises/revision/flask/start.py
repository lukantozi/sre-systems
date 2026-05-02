from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)
token = os.environ["TOKEN"]
headers = {"Authorization": f"Bearer: {token}"}
per_page = 50
params = {"per_page": per_page}

@app.route("/repos")
def get_repos():
    username = request.args.get("username")
    if not username:
        return "<h2>Username missing!!!</h2>\n\
                <h2>Usage: 127.0.0.1:5000/repos?username={your-username}</h2>"
    response = requests.get(
        f"https://api.github.com/users/{username}/repos",
        headers=headers,
        params=params
    )
    if response.status_code != 200:
        return f"<h2>something went wrong</h2>: {response.status_code}"
    response_dict = response.json()
    repos = [
        (repo["full_name"],
         repo["description"] or "No description",
         repo["stargazers_count"],
         repo["html_url"])
        for repo in response_dict]
    return render_template("index.html", repos=repos)
#    return response_dict

app.run()
