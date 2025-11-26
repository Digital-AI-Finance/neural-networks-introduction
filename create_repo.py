import json
import requests
from pathlib import Path

# Read GitHub token from user config
config_path = Path.home() / '.claude' / 'user-config.json'
with open(config_path) as f:
    config = json.load(f)
    token = config.get('github', {}).get('token', '')

if not token:
    print("ERROR: No GitHub token found in ~/.claude/user-config.json")
    exit(1)

# Create repository via GitHub API
url = "https://api.github.com/orgs/Digital-AI-Finance/repos"
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}
data = {
    "name": "neural-networks",
    "description": "Pedagogical Beamer presentation: Neural Networks for Business Applications - Complete course with 20 data-driven visualizations using real trained models",
    "private": False,
    "has_issues": True,
    "has_projects": False,
    "has_wiki": False
}

print("Creating repository Digital-AI-Finance/neural-networks...")
response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    repo_data = response.json()
    print(f"SUCCESS: Repository created at {repo_data['html_url']}")
    print(f"Clone URL: {repo_data['clone_url']}")
elif response.status_code == 422:
    print("Repository already exists!")
    print("Clone URL: https://github.com/Digital-AI-Finance/neural-networks.git")
else:
    print(f"ERROR {response.status_code}: {response.text}")
    exit(1)
