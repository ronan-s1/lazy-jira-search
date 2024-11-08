import subprocess
import webbrowser
from jira import Issue
from typing import List


def select_issue_with_fzf(server_url: str, issues: List[Issue]) -> None:
    """Let the user select an issue using fzf and open the issue in the browser."""
    issue_string = ""
    for issue in issues:
        issue_string += f"{issue.key}: {issue.fields.summary}\n"

    issue_urls = {issue.key: f"{server_url}/browse/{issue.key}" for issue in issues}

    selected_issue = subprocess.run(
        ["fzf", "--exact", "--reverse", "--info=inline", "--height=60%"],
        input=issue_string,
        text=True,
        capture_output=True,
    ).stdout.strip()

    if selected_issue:
        print(f"Selected issue: {selected_issue}")
        issue_key = selected_issue.split(":")[0]
        webbrowser.open(issue_urls[issue_key])
