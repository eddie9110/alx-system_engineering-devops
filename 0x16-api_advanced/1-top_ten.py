#!/usr/bin/python3
""" top ten posts module """
import requests

url = "http://www.reddit.com/r/{}/hot.json"


def top_ten(subreddit):
    """
    Get top ten posts
    """
    res_ponse = requests.get(url.format(subreddit), params={"limit": 10},
                             headers={"User-Agent": "Agent Edwin"},
                             allow_redirects=False)

    if res_ponse.status_code != 200:
        print(None)
        return
    else:
        for post in res_ponse.json().get('data', {}).get('children', []):
            print(post.get('data').get('title'))
