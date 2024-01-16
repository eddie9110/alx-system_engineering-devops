#!/usr/bin/python3
""" module to get reddit subs """

import requests


def number_of_subscribers(subreddit):
    """
    Return the no. of subscribers
    """
    if subreddit is None:
        return 0
    url = "http://www.reddit.com/r/{}/about.json"
    user_agent = {"User-Agent": "Agent Edwin"}
    res_ponse = requests.get(url.format(subreddit), headers=user_agent).json()
    return res_ponse.get("data", {}).get("subscribers", 0)
