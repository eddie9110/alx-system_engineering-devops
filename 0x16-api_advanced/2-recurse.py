#!/usr/bin/python3
""" module of the function recurse """
import requests

url = "http://www.reddit.com/r/{}/hot.json"


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursively queries the Reddit Api and returns the titles of top hot posts

    """
    res_ponse = requests.get(url.format(subreddit), params={"after": after},
                             headers={"User-Agent": "Agent Edwin"},
                             allow_redirects=False)

    if res_ponse.status_code != 200:
        return None
    after = res_ponse.json().get("data").get("after")
    if not after:
        return hot_list
    for post in res_ponse.json().get("data").get("children"):
        hot_list.append(post.get("data").get("title"))
    return recurse(subreddit, hot_list, after)
