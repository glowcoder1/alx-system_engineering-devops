#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first ten (10) hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    queries the Reddit API prints the titles of the first 10 hot posts
    - If not a valid subreddit, print None.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if req.status_code == 200:
        for item in req.json().get("data").get("children"):
            data = item.get("data")
            title = data.get("title")
            print(title)
    else:
        print(None)
