import requests

def fetch_commit_data(user, repo):
    url = f"https://api.github.com/repos/seejnn/Algorithm-Study/contributors"
    response = requests.get(url)
    return response.json()

def extract_top_committer(data):
    # Process data to find the top committer
    top_committer = max(data, key=lambda x: x['contributions'])
    return top_committer['login'], top_committer['contributions']

def update_readme(user, repo, top_committer, commits):
    readme_content = f"# Repository Stats\n\n- Top Committer: {top_committer} with {commits} commits."
    # Code to update README.md on GitHub
    # This could be done using the GitHub API or by cloning the repo, updating the file, and pushing the changes

user = "username"
repo = "repository"
data = fetch_commit_data(user, repo)
top_committer, commits = extract_top_committer(data)
update_readme(user, repo, top_committer, commits)
