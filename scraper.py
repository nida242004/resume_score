import requests

def scrape_github_projects():
    username = 'YOUR_GITHUB_USERNAME'  # Replace with your GitHub username
    token = 'YOUR_PERSONAL_ACCESS_TOKEN'  # Replace with your GitHub personal access token

    url = f'https://api.github.com/users/nida242004/repos'
    response = requests.get(url, auth=(username, token))

    if response.status_code != 200:
        raise Exception(f"Failed to fetch repositories: {response.status_code}")

    projects = []
    repos = response.json()

    for repo in repos:
        name = repo['name']
        link = repo['html_url']
        description = repo['description'] if repo['description'] else "No description"
        created_at = repo['created_at']  # Fetch creation date
        tech_stack = repo.get('language', 'Not specified')

        projects.append({
            'name': name,
            'link': link,
            'description': description,
            'created_at': created_at,
            'tech_stack': tech_stack
        })

    # Sort projects by creation date (latest first)
    projects.sort(key=lambda x: x['created_at'], reverse=True)

    return projects
