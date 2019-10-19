# Aprola Tutorials Git Commands:

### to clone: git clone <url_for_clone>

```
git clone https://github.com/aprola/aprola-tutorials.git
```

### to make branch: git checkout -b <new_branch_name>

```
git checkout -b test_branch_name
```

### to check status: git status

```
git status
```

### to stage files to commit: git add <filePath1> <filePath2> | .

```
# to add files individually
git add ./run.py ./test.py

# to add all files reflected in git status
git add .
```

### to commit with message: git commit -m <message>

```
git commit -m "write brief description about the commit"
```


### to check commit logs of current branch: git logs

```
git logs
```


### to push commit : git push -u <remote_name> <local_branch_name>

```
git push -u origin test_branch_name
```

### to rebases with another branch : git rebase <remote_or_local_branch>

to make branch merge ready with master. ie if the master branch moved ahead with new changes we need to replay our
branch to the same head so that the merge is done without loosing exising new changes.

we need to do following steps in sequence.

1. make sure you dont have any changes to commit. ie. git status shouldnt show any changes.
2. Get the latest version of git from remote(github) to local git with - ```git fetch
3. if any confits arise in rebase. resolve them using vscode.
  3.1. resolve the conflicts
  3.2. continue rebase
4. Force push the code to the git remote: git push -u <remote_name> <local_branch_name>

```
# 1. check
git status 
# 2. fetch the new changes from remote
git fetch
# 3. rebase
git rebase origin/master
# 3.2
git rebase --continue
# 4
git push -u origin test_branch_name -f
```
