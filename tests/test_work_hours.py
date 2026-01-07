from datetime import datetime
from gitcommitinsight.checks.work_hours import analyze_work_hours


def test_off_hour_commit():
    commits = [{
        "hash": "abc123",
        "date": datetime(2024, 1, 1, 22, 30)
    }]

    result = analyze_work_hours(commits)
    assert "abc123" in result
