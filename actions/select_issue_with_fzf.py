import subprocess
import webbrowser
from jira import Issue
from typing import List


def select_issue_with_fzf(jira_server: str, issues: List[Issue]) -> None:
    """Let the user select one or more issues using fzf and open them in the browser."""
    issue_string = "\n".join(f"{issue.key}: {issue.fields.summary}" for issue in issues)
    issue_urls = {issue.key: f"{jira_server}/browse/{issue.key}" for issue in issues}

    selected_issues = subprocess.run(
        ["fzf", "--multi", "--exact", "--reverse", "--info=inline", "--height=60%"],
        input=issue_string,
        text=True,
        capture_output=True,
    ).stdout.strip()

    if selected_issues:
        issue_keys = [line.split(":")[0] for line in selected_issues.split("\n")]
        for issue_key in issue_keys:
            webbrowser.open(issue_urls[issue_key])
