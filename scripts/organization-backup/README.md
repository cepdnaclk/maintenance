## GitHub Organization Backup - cepdnaclk

- We are keeping a backup of all the `public` GitHub repositories under the organization.
- The backup is stored in { FILL THIS }.
- This backup will be taken at { TIME, FREQUENCY }, using the method, { METHOD}


#### Process Explanation

- First the Python script, `generate.py` will use GitHub APIs to prepare a list of Repos, and stored it in './backup/repos.json'
- Next, the same Python script will generate a BASH file, `./backup/execute.sh` with the necessary commands to clone/pull the repositories 
  - If a repository already exists, it will only `pull` the changes.
  - Otherwise, it will `clone` the repository.
