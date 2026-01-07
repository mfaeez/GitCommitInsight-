from gitcommitinsight.checks.bad_messages import analyze_bad_messages
from gitcommitinsight.checks.commit_frequency import analyze_commit_frequency
from gitcommitinsight.checks.commit_size import analyze_commit_size
from gitcommitinsight.checks.dead_days import analyze_dead_days
from gitcommitinsight.checks.work_hours import analyze_work_hours


def run_analysis(commits):
    return {
        "frequency": analyze_commit_frequency(commits),
        "dead_days": analyze_dead_days(commits),
        "bad_messages": analyze_bad_messages(commits),
        "large_commits": analyze_commit_size(commits),
        "off_hour_commits": analyze_work_hours(commits),
    }

