from typing import List
from jira import Issue
from datetime import datetime
from actions import (
    BOLD,
    RESET_BOLD,
    GREEN,
    PINK,
    YELLOW,
    HYPERLINK_START,
    HYPERLINK_END,
    RESET_COLOUR,
)


def print_issues(server_url: str, issues: List[Issue], verbose: bool = False) -> None:
    """Display user"s issues with clickable, green-coloured keys."""
    print_str = ""
    for issue in issues:
        issue_url = f"{server_url}/browse/{issue.key}"
        clickable_key = (
            f"{BOLD}{HYPERLINK_START}{issue_url}{HYPERLINK_END}"
            f"{GREEN}{issue.key}{RESET_COLOUR}"
            f"{HYPERLINK_START}{HYPERLINK_END}{RESET_BOLD}"
        )

        # Parse and format the last updated date
        last_updated_formatted = f"{PINK}{datetime.strptime(issue.fields.updated, '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%-d %b %Y')}{RESET_COLOUR}"

        print_str += (
            f"\n{clickable_key} ({last_updated_formatted}): {issue.fields.summary}"
        )

    if verbose:
        print(
            f"\n{BOLD}Assigned To You {YELLOW}({len(issues)} results){RESET_COLOUR}:{RESET_BOLD}"
        )

    print(print_str)
