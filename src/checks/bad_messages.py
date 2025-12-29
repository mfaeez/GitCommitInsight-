from src.config import BAD_COMMIT_KEYWORDS

def detect_bad_commit_messages(commits):
    bad = []

    for c in commits:
        msg = c["message"].lower()
        if any(word in msg for word in BAD_COMMIT_KEYWORDS):
            bad.append({
                "hash": c["hash"],
                "message": c["message"]
            })

    return bad
