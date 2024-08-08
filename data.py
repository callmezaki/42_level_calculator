import json
with open('assets/project_data.json') as f:
    data = json.load(f)

projects = {}

for obj in data:
    # store name and xp of all projects
    projects[obj['name']] = obj['difficulty']
