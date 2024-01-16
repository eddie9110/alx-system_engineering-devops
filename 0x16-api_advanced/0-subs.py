#!/usr/bin/python3
""" module to get reddit subs """

import requests

url = "http://www.reddit.com/r/{}/about.json"


def number_of_subscribers(subreddit):
    """
    Return the no. of subscribers
    """
    if subreddit is None:
        return 0
    res_ponse = requests.get(url.format(subreddit),
                             headers={"User-Agent": "Agent Edwin"})
    return res_ponse.json().get("data", {}).get("subscribers", 0)
