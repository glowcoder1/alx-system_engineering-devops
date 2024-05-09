#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    recursive function that queries the Reddit API
    - returns a list containing the titles of all hot articles for a given subreddit
    - If not a valid subreddit, return None.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if req.status_code == 200:
        for item in req.json().get("data").get("children"):
            data = item.get("data")
            title = data.get("title")
            hot_list.append(title)
        after = req.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
