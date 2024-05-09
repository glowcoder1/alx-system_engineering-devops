#!/usr/bin/python3
""" returns subscripber count"""

import requests
import sys


def number_of_subscribers(subreddit):
    if subreddit is None:
        return None
    req = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                       headers={"User-Agent": "Custom"})
    if req.status_code == 200:
        res = req.json().get("data")
        subs = res.get("subscribers")
        if subs:
            return res.get("subscribers")
        return 0
