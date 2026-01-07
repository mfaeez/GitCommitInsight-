import argparse
from gitcommitinsight.core.analyzer import run_analysis
from gitcommitinsight.core.git_reader import read_commits
from gitcommitinsight.core.report import generate_report


def main():
    parser = argparse.ArgumentParser(description="Git Commit Insight")
    parser.add_argument("--repo", default=".", help="Path to git repo")

    args = parser.parse_args()

    commits = read_commits(args.repo)
    results = run_analysis(commits)
    report_path = generate_report(results)

    print(f"Report generated at: {report_path}")


if __name__ == "__main__":
    main()
