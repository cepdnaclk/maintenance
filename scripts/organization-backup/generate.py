# Please note that this is implemented for targetting Linux environment

import requests
import os
import json

ORGANIZATION = "cepdnaclk"
pwd = os.getcwd() + "/backup"


def urlOrganizationRepos(pageNo):
    return "https://api.github.com/orgs/{0}/repos?page={1}".format(ORGANIZATION, pageNo)


# Let's always run this for now
if True or not os.path.exists("./backup/repos.json"):
    # Already have the
    print("Downloading repo data...")
    r = requests.get(
        url="https://api.github.com/orgs/{0}".format(ORGANIZATION))
    j = r.json()

    repos = []

    # Handle the pagination
    for p in range(1, 1000):
        r = requests.get(url=urlOrganizationRepos(p))
        jsonData = r.json()

        repos.extend(jsonData)

        print("Page:{0}, Repos: {1}, Total:{2}".format(
            p, len(jsonData), len(repos)))

        if len(jsonData) == 0:
            break

    # Sort the repos
    repos.sort(key=lambda x: x['name'])

    # Store the result
    filename = "./backup/repos.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(json.dumps(repos, indent=4))

else:
    print("Loading repo data...")
    url = './backup/repos.json'
    with open(url, 'r') as f:
        repos = json.load(f)


# Generate the execution script
counter = 0
count = len(repos)
script_file = []

for r in repos:
    repo_url = r['html_url']
    repo_name = r['name']
    path = "./backup/{}".format(repo_name)

    print(repo_name)

    counter += 1
    # if counter > 5:
    #     break

    script_file.append("echo \"\"")
    script_file.append("echo \"{:>3}/{:>3}\"".format(counter, count))

    if os.path.exists(path):
        # Already cloned, therefore only updating
        script_file.append("echo \"Synchronizing \t{0}\"".format(repo_name))
        script_file.append(
            "cd {}/{} && git pull && cd ../".format(pwd, repo_name))
        # os.system("cd {} && git pull".format(path))
    else:
        # New repository, need to be clone
        script_file.append("echo \"Downloading \t{0}\"".format(repo_name))
        script_file.append(
            "cd {} && git clone {} --depth 1".format(pwd, repo_url))
        #  os.system("cd './backup/' && git clone {}".format(repo_url))


script_file.append("mv -f -T ./repos.json ./repos_backuped.json\"\"")

script_file.append("echo \"\"")
script_file.append("echo \"Backup completed.....\"")

# TODO: Print the backup size
# du -sh ./

# Save the execute file
execute_file = "./backup/execute.sh"
os.makedirs(os.path.dirname(execute_file), exist_ok=True)
f = open(execute_file, "w")
f.write("\n".join(script_file))
