from datetime import timedelta
from src.utils import parse_git_date, format_day

def detect_dead_days(commits):
    dates = sorted(set(
        parse_git_date(c["date"]).date()
        for c in commits
    ))

    dead = []
    for i in range(len(dates) - 1):
        gap = (dates[i+1] - dates[i]).days
        if gap > 1:
            for d in range(1, gap):
                dead.append(format_day(dates[i] + timedelta(days=d)))

    return dead
