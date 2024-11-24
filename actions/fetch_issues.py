from jira import JIRA, Issue
from typing import List, Optional
from actions import BOLD, RESET_BOLD

JIRA_QUERY_DEFAULT = "assignee = {assignee} AND resolution = Unresolved"
JIRA_QUERY_RESOLVED = "assignee = {assignee} AND resolution != Unresolved"
JIRA_QUERY_ALL = "assignee = {assignee}"
JIRA_QUERY_SORTED = " ORDER BY updated DESC"
JIRA_QUERY_TIME_RANGE = " AND updated >= -{time}"


def fetch_issues(
    jira_client: JIRA,
    sort_by_updated: bool = False,
    time: bool = False,
    resolved: bool = False,
    verbose: bool = False,
    all_issues: bool = False,
    assignee: str = None,
    reporter: str = None,
    max_results: int = 200,
) -> List[Issue]:
    """Fetch issues based on arguments passed."""
    # Default assignee to current user if not specified
    assignee = assignee.lower()

    # Main filters
    query_to_use = JIRA_QUERY_DEFAULT.format(assignee=assignee)
    if all_issues:
        query_to_use = JIRA_QUERY_ALL.format(assignee=assignee)
    if resolved:
        query_to_use = JIRA_QUERY_RESOLVED.format(assignee=assignee)
    if reporter:
        reporter_filter = f" AND reporter = {reporter}"
        query_to_use += reporter_filter
    if time:
        query_to_use += JIRA_QUERY_TIME_RANGE
        query_to_use = query_to_use.format(time=time)
    if sort_by_updated:
        query_to_use += JIRA_QUERY_SORTED

    # After query built
    if assignee == "none":
        query_to_use = query_to_use.replace("assignee = none AND ", "")
    if verbose:
        print(f"\n{BOLD}Query:{RESET_BOLD} {query_to_use}")

    print(max_results)
    return jira_client.search_issues(jql_str=query_to_use, maxResults=max_results)
