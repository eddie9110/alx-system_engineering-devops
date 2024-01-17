#!/usr/bin/python3
""" module to get reddit subs """

import requests


def number_of_subscribers(subreddit) -> int:
    """
    Return the no. of subscribers
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        request = requests.get(url, headers={'User-Agent': 'Agent Edwin'})
        response = request.json()
        return response['data']['subscribers']
    except Exception:
        return 0
