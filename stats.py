# import requests

# def fetch_commit_data(user, repo):
#     url = f"https://api.github.com/repos/seejnn/Algorithm-Study/contributors"
#     response = requests.get(url)
#     return response.json()

# def extract_top_committer(data):
#     # Process data to find the top committer
#     top_committer = max(data, key=lambda x: x['contributions'])
#     return top_committer['login'], top_committer['contributions']

# def update_readme(user, repo, top_committer, commits):
#     readme_content = f"# Repository Stats\n\n- Top Committer: {top_committer} with {commits} commits."
#     # Code to update README.md on GitHub
#     # This could be done using the GitHub API or by cloning the repo, updating the file, and pushing the changes

# user = "username"
# repo = "repository"
# data = fetch_commit_data(user, repo)
# top_committer, commits = extract_top_committer(data)
# update_readme(user, repo, top_committer, commits)




import requests
import os
from github import Github

def fetch_commit_data(token, user, repo):
    # Authenticating with GitHub
    g = Github(token)
    repo = g.get_repo(f"{user}/{repo}")
    contributors = repo.get_contributors()
    return contributors

def extract_top_committer(contributors):
    top_committer = max(contributors, key=lambda x: x.contributions)
    return top_committer.login, top_committer.contributions

def update_readme(token, user, repo, top_committer, commits):
    # Authenticating with GitHub
    g = Github(token)
    repo = g.get_repo(f"{user}/{repo}")

#     # Update README
#     readme_content = f"

# ## 사용법
# 1. BaekjoonHub 크롬 확장 프로그램 설치 (@seejnn 에게 문의주세요)
# 2. Github 계정 연동
# 3. 알고리즘 스터디 repository 연동

# 위의 과정을 마친 후 

# 백준 / 프로그래머스 / SWEA 에서 문제를 풀면 자동으로

# 해당 문제 정보와 작성한 코드가 레포지토리에 업로드됩니다.

# <br />

# 현재는 BaekjoonHub의 기본 설정인 난이도별로 디렉토리가 설정됩니다.


# # 커밋 순위 \n\n- 1등: {top_committer} - {commits} 커밋\n"
#     readme_file = repo.get_contents("README.md", ref="main")
#     repo.update_file(readme_file.path, "Update top committer stats", readme_content, readme_file.sha)

# # GitHub Personal Access Token
# token = os.getenv('GITHUB_TOKEN')

# user = "seejnn"
# repo = "Algorithm-Study"
# contributors = fetch_commit_data(token, user, repo)
# top_committer, commits = extract_top_committer(contributors)
# update_readme(token, user, repo, top_committer, commits)















# Fetching current README content
    readme_file = repo.get_contents("README.md", ref="main")
    current_content = readme_file.decoded_content.decode("utf-8")

    # Appending the top committer information
    updated_content = current_content + f"\n- 1등: {top_committer} - {commits} 커밋\n"

    # Update README
    repo.update_file(readme_file.path, "Update top committer stats", updated_content, readme_file.sha)

# GitHub Personal Access Token
token = os.getenv('GITHUB_TOKEN')

user = "seejnn"
repo = "Algorithm-Study"
contributors = fetch_commit_data(token, user, repo)
top_committer, commits = extract_top_committer(contributors)
update_readme(token, user, repo, top_committer, commits)
