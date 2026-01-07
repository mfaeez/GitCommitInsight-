import subprocess
from datetime import datetime


def read_commits(repo_path="."):
    command = [
        "git",
        "log",
        "--pretty=format:%H|%an|%ad|%s",
        "--date=iso",
    ]

    result = subprocess.check_output(command, cwd=repo_path).decode()
    commits = []

    for line in result.splitlines():
        commit_hash, author, date, message = line.split("|", 3)
        commits.append({
            "hash": commit_hash,
            "author": author,
            "date": datetime.fromisoformat(date),
            "message": message,
        })

    return commits

