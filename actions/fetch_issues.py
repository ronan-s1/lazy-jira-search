from jira import JIRA, Issue
from typing import List
from actions import BOLD, RESET_BOLD

JIRA_QUERY_DEFAULT = "assignee = {current_user} AND resolution = Unresolved"
JIRA_QUERY_RESOLVED = "assignee = {current_user} AND resolution != Unresolved"
JIRA_QUERY_ALL = "assignee = {current_user}"
JIRA_QUERY_SORTED = " ORDER BY updated DESC"
JIRA_QUERY_TIME_RANGE = " AND updated >= -{time}"


def fetch_issues(
    jira_client: JIRA, sort_by_updated: bool = False, time: bool = False, resolved = False, verbose: bool = False, all_issues: bool = False
) -> List[Issue]:
    """Fetch issues based on flags passed."""
    current_user = jira_client.current_user()

    query_to_use = JIRA_QUERY_DEFAULT.format(current_user=current_user)

    if all_issues:
        query_to_use = JIRA_QUERY_ALL.format(current_user=current_user)
    if resolved:
        query_to_use = JIRA_QUERY_RESOLVED.format(current_user=current_user)
    if time:
        query_to_use += JIRA_QUERY_TIME_RANGE
        query_to_use = query_to_use.format(time=time)
    if sort_by_updated:
        query_to_use += JIRA_QUERY_SORTED

    if verbose:
        print(f"\n{BOLD}Query:{RESET_BOLD} {query_to_use}")

    return jira_client.search_issues(query_to_use)
