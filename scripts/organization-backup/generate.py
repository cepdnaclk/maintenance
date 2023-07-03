import requests
import os
import json

ORGANIZATION = "cepdnaclk"


def urlOrganizationRepos(pageNo):
    return "https://api.github.com/orgs/{0}/repos?page={1}&per_page=100".format(ORGANIZATION, pageNo)


if not os.path.exists("./backup/repos.json"):
    print("Downloading repo data...")
    r = requests.get(
        url="https://api.github.com/orgs/{0}".format(ORGANIZATION))
    j = r.json()

    repos = []

    for p in range(1, 1000):
        r = requests.get(url=urlOrganizationRepos(p))
        jsonData = r.json()

        repos.extend(jsonData)

        print("Page:{0}, Repos: {1}, Total:{2}".format(
            p, len(jsonData), len(repos)))

        if len(jsonData) == 0:
            break

    filename = "./backup/repos.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(json.dumps(repos, indent=4))

else:
    print("Loading repo data...")
    url = './backup/repos.json'
    with open(url, 'r') as f:
        repos = json.load(f)

counter = 0
count = len(repos)
script_file = []

for r in repos:
    repo_url = r['html_url']
    repo_name = r['name']
    path = "./backup/{}".format(repo_name)

    counter += 1
    # if counter > 5:
    #     break

    script_file.append("echo \"\"")
    script_file.append("echo \"{:>3}/{:>3}\"".format(counter, count))

    if os.path.exists(path):
        script_file.append("echo \"Synchronizing \t{0}\"".format(repo_name))
        script_file.append("cd ./{} && git pull && cd ../".format(repo_name))
        # os.system("cd {} && git pull".format(path))
    else:
        script_file.append("echo \"Downloading \t{0}\"".format(repo_name))
        script_file.append("git clone {} --depth 1".format(repo_url))
        #  os.system("cd './backup/' && git clone {}".format(repo_url))


execute_file = "./backup/execute.sh"
os.makedirs(os.path.dirname(execute_file), exist_ok=True)
f = open(execute_file, "w")
f.write("\n".join(script_file))
