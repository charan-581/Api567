import requests
import json

def get_repo_info(user_id):
    if not isinstance(user_id, str):
        return {}
    if user_id == "" or user_id.isdigit() or user_id == "! ":
        return {}    
    response = requests.get("https://api.github.com/users/"+ user_id +"/repos")
    # API timed out or no repo or invalid user id
    if response.status_code != 200 or response.status_code == 403 or response.status_code == 404:
        return {}
    repoinfo = {}
    repodata = json.loads(response.text)
    for repo in repodata:
        reponame = repo.get("name")
        cr = requests.get("https://api.github.com/repos/" + user_id + "/" + reponame + "/commits")
        # API timed out or no repo or invalid request
        if cr.status_code != 200 or cr.status_code == 403 or cr.status_code == 404:
            return {}
        cc = len(json.loads(cr.text))
        repoinfo[reponame] = cc
    return repoinfo

if __name__ == "__main__":
    user_id = input("Enter the user id: ")
    repositories = get_repo_info(user_id)
    if repositories:
        for repo, commits in repositories.items():
            print("Repo: {} Number of commits: {}".format(repo, commits))