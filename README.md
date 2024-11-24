# Lazy Jira Search
A CLI tool to find your Jira tickets faster.

## Problem Statement
Sometimes I forget what tickets I have, especially if they're across different boards or lost in the backlog. This tool speeds up this process and helps you find tickets that are assigned to you quickly.

Also Jira's UI is just painfully slow, lots of clicking around, lots of waiting, lots time wasted and I am lazy so I ain't doin allat. I'm not sure how useful this will even be but shall see.

## Usage
By default (passing no arguments), you will see all unresolved Jira issues assigned to you. You can change this behaviour by passing in different arguments shown below.

### Arguments
`-f, --fzf`: Pipe output to fzf for interactive selection.

`-a, --all`: Display all issues assigned to you.

`-t, --time`: Filter issues updated in the last x amount of time. Supported units: d (days), w (weeks), m (months).

`-s, --sort`: Sort issues by last updated time in descending order.

`-as, --assignee`: Filter issues by specified assignee.

`-rep, --reporter`: Filter issues by the specified reporter; defaults to you if no value is provided.

`-r, --resolved`: Display issues already resolved.

`-m, --max`: Max amount of issues to fetch (default is 200).

`-v, --verbose`: Enable verbose output.

`-h, --help`: Display usable flags.

Clicking the issue key or selecting it in fzf will open it in your browser

## Example
The below command will:
- Find unresolved Jiras assigned to you
- Last updated in the last 2 weeks
- Sorted in descending order by last updated
- Pipe into fzf for quick searching

```
lazy -t 2w -s -f
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
