# Lazy Jira Search
A CLI tool to find your Jira tickets faster.

## Problem Statement
People often lose track tickets, especially when they're spread across multiple boards or buried in the backlog. This tool simplifies the process, making it easy to quickly find tickets assigned to you or any other ticket.

TBH, Jira's UI is also painfully slow, with lots licking, waiting which wastes time. This tool removes all that toil.

## Usage
By default (passing no arguments), you will see all unresolved Jira issues assigned to you:

```
assignee = <your username> AND resolution = Unresolved
```

You can change this behaviour by passing in different arguments shown below.

### Arguments
`-f, --fzf`: Pipe output to fzf for interactive selection.

`-a, --all`: Display all issues assigned to you.

`-t, --time`: Filter issues updated in the last x amount of time. Supported units: d (days), w (weeks), m (months).

`-s, --sort`: Sort issues by last updated time in descending order.

`-as, --assignee`: Filter issues by specified assignee. Pass "none" to remove assignee filter.

`-rep, --reporter`: Filter issues by the specified reporter; defaults to you if flag is used but no value is provided.

`-r, --resolved`: Display issues already resolved.

`-m, --max`: Max amount of issues to fetch (default is 200).

`-v, --verbose`: Enable verbose output.

`-h, --help`: Display usable flags.

### NOTE
- You are always the assignee unless specified by `--assignee` flag.
- Unresolved issues will be fetched unless specified by `--all` or `--resolved` flags.
- You are the reporter if `--reporter` is used but no value is passed.
- Passing **"none"** for the assignee will remove the assignee filter entirely.
- Clicking the issue key or selecting it in fzf view will open it in your browser.
- You can hit tab to select multiple issues in `--fzf` mode.

## Examples

### Example 1
The below command will:
- Find unresolved Jiras assigned to you
- Last updated in the last 2 weeks
- Sorted in descending order by last updated
- Pipe into fzf for quick searching

```
lazy -t 2w -s -f
```

It's equivalent to using this JQL query (but without the slowlness of Jira's interface):

```
assignee = <your username> AND resolution = Unresolved AND updated >= -2w ORDER BY updated DESC
```

### Example 2

```bash
lazy -rep -as none
```

```
resolution = Unresolved AND reporter = <your username>
```

## Set up
1. Install libraries
    ```bash
    pip install -r requirements.txt
    ```

2. Install [fzf](https://github.com/junegunn/fzf?tab=readme-ov-file#installation) (on mac)
    ```
    brew install fzf
    ```

3. If using bash add this to your `~/.bashrc`:
    ```bash
    eval "$(fzf --bash)"
    ```

   If zsh, add this to your `~/.zshrc`:
    ```bash
    source <(fzf --zsh)
    ```

4. create `.env` (see `.env.example`)
    ```
    API_TOKEN=<PAT>
    JIRA_SERVER=<JIRA_SERVER>
    ```

5. Set up an alias in your `~/.bashrc` or `~/.zshrc`:
    ```bash
    alias lazy="python /path/to/lazy-jira-search/main.py"
    ```

### To Do
- filter by assignee and reporter
- rewrite in go 💀
