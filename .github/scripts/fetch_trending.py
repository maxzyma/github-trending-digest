#!/usr/bin/env python3
"""Fetch GitHub Trending page and output structured JSON.

Usage:
    python fetch_trending.py [--date YYYY-MM-DD] [--previous PATH]

Output (stdout): JSON array of trending repos with optional ranking changes.
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime


def fetch_html():
    """Fetch trending page HTML using gh auth token for authentication."""
    try:
        token = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        token = None

    cmd = ["curl", "-s", "https://github.com/trending?since=daily"]
    if token:
        cmd += ["-H", f"Authorization: token {token}"]
    cmd += ["-H", "User-Agent: Mozilla/5.0", "-H", "Accept: text/html"]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    return result.stdout


def parse_repos(html):
    """Extract repo data from trending page HTML."""
    repos = re.findall(r'href="/([^/]+/[^/]+)/stargazers', html)
    stars_today = re.findall(r'([\d,]+)\s+stars today', html)
    langs = re.findall(r'itemprop="programmingLanguage"[^>]*>([^<]+)', html)
    descs = re.findall(r'<p class="col-9[^>]*>\s*([^\n<]+)', html)

    results = []
    for i, repo in enumerate(repos):
        results.append({
            "rank": i + 1,
            "repo": repo.strip(),
            "language": langs[i].strip() if i < len(langs) else "",
            "stars_today": stars_today[i].strip() if i < len(stars_today) else "",
            "description": descs[i].strip() if i < len(descs) else "",
        })
    return results


def load_previous(path):
    """Load previous day's markdown file and extract repo list."""
    prev_repos = []
    try:
        with open(path) as f:
            for line in f:
                parts = line.split("|")
                if len(parts) >= 4:
                    repo = parts[2].strip()
                    if "/" in repo and not repo.startswith("-"):
                        prev_repos.append(repo)
    except FileNotFoundError:
        pass
    return prev_repos


def compute_changes(current, previous):
    """Add ranking change info to current repos based on previous list."""
    prev_map = {r: i + 1 for i, r in enumerate(previous)}
    for repo in current:
        name = repo["repo"]
        if name in prev_map:
            old_rank = prev_map[name]
            new_rank = repo["rank"]
            if old_rank == new_rank:
                repo["change"] = "="
            elif new_rank < old_rank:
                repo["change"] = f"↑{old_rank - new_rank}"
            else:
                repo["change"] = f"↓{new_rank - old_rank}"
        else:
            all_prev = set(previous)
            # Check if it appeared in any historical file (RE vs NEW)
            repo["change"] = "NEW"
    return current


def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub Trending data")
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"),
                        help="Date label (default: today)")
    parser.add_argument("--previous", help="Path to previous day's .md file")
    args = parser.parse_args()

    html = fetch_html()
    if not html:
        print(json.dumps({"error": "Failed to fetch trending page"}))
        sys.exit(1)

    repos = parse_repos(html)
    if not repos:
        print(json.dumps({"error": "No repos found in HTML", "html_length": len(html)}))
        sys.exit(1)

    if args.previous:
        previous = load_previous(args.previous)
        repos = compute_changes(repos, previous)

    weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    d = datetime.strptime(args.date, "%Y-%m-%d")
    weekday = weekdays[d.weekday()]

    output = {
        "date": args.date,
        "weekday": weekday,
        "count": len(repos),
        "repos": repos,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
