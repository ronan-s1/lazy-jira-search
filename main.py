import argparse
import os
from jira import JIRA
from dotenv import load_dotenv
from actions.print_issues import print_issues
from actions.fetch_issues import fetch_issues
from actions.select_issue_with_fzf import select_issue_with_fzf

# Constants
ENV_FILE_PATH = os.path.join(os.path.dirname(__file__), ".env")


def get_jira_client(jira_server: str) -> JIRA:
    """Initialise and return the JIRA client."""
    return JIRA(options={"server": jira_server}, token_auth=os.getenv("API_TOKEN"))


def main() -> None:
    # Load environment vars
    load_dotenv(ENV_FILE_PATH)
    jira_server = os.getenv("JIRA_SERVER")

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fzf", action="store_true", help="Pipe output to fzf")
    parser.add_argument(
        "-s",
        "--sort",
        action="store_true",
        help="Sort issues by last updated in descending order",
    )
    parser.add_argument(
        "-t",
        "--time",
        type=str,
        help="Filter issues updated within the last [X] time period (e.g., 5d, 2w, 1m)",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )
    parser.add_argument(
        "-r", "--resolved", action="store_true", help="Fetch all resolved issues"
    )
    parser.add_argument(
        "-a", "--all", action="store_true", help="Fetch all issues ever assigned to you"
    )
    args = parser.parse_args()

    # Initialise JIRA client
    jira_client = get_jira_client(jira_server=jira_server)

    # Fetch issues
    issues = fetch_issues(
        jira_client,
        sort_by_updated=args.sort,
        time=args.time,
        resolved=args.resolved,
        verbose=args.verbose,
        all_issues=args.all,
    )

    # Display issues or select with fzf
    if args.fzf:
        select_issue_with_fzf(jira_server=jira_server, issues=issues)
    else:
        print_issues(jira_server=jira_server, issues=issues, verbose=args.verbose)


if __name__ == "__main__":
    main()
