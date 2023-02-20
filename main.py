import requests
import json

YOUR_TOKEN = ""
ORG = ''
USERNAME = ''

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {YOUR_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}

GET_REPO_LIST = f'https://api.github.com/orgs/{ORG}/repos?per_page=100'

r = requests.get(GET_REPO_LIST, headers=headers)
repo_list_str = r.text
with open('lists.json', 'w') as file:
    file.write(repo_list_str)
read = open('lists.json')
repo_list = json.load(read)
i = 1
for repo in repo_list:
    REPO = repo['name']
    URL = f'https://api.github.com/repos/{ORG}/{REPO}/collaborators/{USERNAME}'
    r = requests.delete(url=URL, headers=headers)
    print(f'{i}Код ответа {r}: пользлватель {USERNAME} удален из {REPO}')
    i = i + 1

